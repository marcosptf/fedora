# -*- coding: utf-8 -*-

"""
Copyright (C) 2010 Dariusz Suchojad <dsuch at gefira.pl>

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

# stdlib
from logging.handlers import SysLogHandler
import glob, imp, logging, logging.config, os, subprocess, sys, syslog, uuid

# Spring Python
from springpython.context import ApplicationContext

# sec-wall
from secwall import app_context
from secwall.core import LoggingFormatter
from secwall.server import HTTPProxy, HTTPSProxy

# A crude hack, no doubt, but otherwise sec-wall on Python 2.7/Fedora (other
# systems presumably as well) bails out when starting.
subprocess._has_poll = False

class _Command(object):
    """ A base class for all CLI commands.
    """

    # Some commands need direct access to the configuration module,
    # thus if 'needs_config_mod' is not False, the config will be read in
    # the command's __init__ method.
    needs_config_mod = True

    # A directory containing a file of that name will be considered to
    # be a sec-wall's config directory.
    _config_marker = '.sec-wall-config'

    def __init__(self, config_dir, app_ctx, is_https):
        config_dir = os.path.abspath(config_dir)
        if not os.path.exists(config_dir):
            msg = "Path {0} doesn't exist.\n".format(config_dir)
            self._error(msg, False)

        self.config_dir = config_dir
        self.app_ctx = app_ctx
        self.is_https = True if is_https and int(is_https) else False

        if self.needs_config_mod:
            self.config_mod = self._get_config_mod()

    def _zdaemon_command(self, zdaemon_command, conf_file):
        """ A somewhat higher-level wrapper for executing zdaemon's commands.
        """
        conf_file = os.path.abspath(os.path.join(self.config_dir, conf_file))
        pid = self._execute_zdaemon_command(['zdaemon', '-C', conf_file, zdaemon_command])

        if zdaemon_command == 'stop':
            os.remove(conf_file)

        return pid

    def _execute_zdaemon_command(self, command_list):
        """ A low-level wrapper for executing zdaemon's commands through
        subprocesses and pipes (doesn't talk directly to the zdaemon's socket).
        """
        p = subprocess.Popen(command_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        p.wait()

        if p.returncode is None:
            msg = 'Could not execute command {0} (p.returncode is None)'
            msg = msg.format(command_list)
            raise Exception(msg)

        else:
            if p.returncode != 0:
                stdout, stderr = p.communicate()
                msg = 'Failed to execute command {0}.'
                msg += ' return code=[{1}], stdout=[{2}], stderr=[{3}]'
                msg = msg.format(command_list, p.returncode, stdout, stderr)
                raise Exception(msg)

            stdout, stderr = p.communicate()
            if stdout.startswith('program running'):
                data = stdout
                data = data.split(';')[1].strip()
                pid = data.split('=')[1].strip()

                return pid

    def _get_config_mod(self):
        """ Return a fully initialized, ready to use, config module. Any missing
        values are filled in with defaults from the app context.
        """

        marker_path = os.path.normpath(os.path.join(self.config_dir, self._config_marker))
        if not os.path.exists(marker_path):
            msg = "The {0} file is missing,".format(self._config_marker)
            msg += " are you sure {0} is a sec-wall's".format(self.config_dir)
            msg += ' config directory?\n'
            self._error(msg)

        f, p, d = imp.find_module('config', [self.config_dir])
        config_mod = imp.load_module('config', f, p, d)

        names = ('server_type', 'host', 'port', 'log', 'crypto_dir', 'keyfile',
                 'certfile', 'ca_certs', 'not_authorized', 'forbidden',
                 'no_url_match', 'internal_server_error', 'validation_precedence',
                 'client_cert_401_www_auth', 'syslog_facility', 'syslog_address', 'log_level', 'log_file_config',
                 'server_tag', 'instance_name', 'quote_path_info', 'quote_query_string',
                 'from_backend_ignore', 'add_invocation_id', 'sign_invocation_id',
                 'default_url_config', 'add_default_if_not_found')

        for name in names:
            attr = getattr(config_mod, name, None)
            if not attr:
                attr = self.app_ctx.get_object(name)
                setattr(config_mod, name, attr)

        return config_mod

    def _error(self, msg, use_prefix=True):
        """ A utility method for printing the error message and quiting the app.
        """
        if use_prefix:
            msg = "Couldn't start sec-wall. " + msg

        sys.stderr.write(msg)
        sys.exit(3)

    def run(self):
        """ Actually runs the command. Must be overridden in subclasses.
        """
        raise NotImplementedError()

class Init(_Command):
    """ Handles the 'sec-wall --init /path/to/config/dir' command.
    """
    needs_config_mod = False

    def run(self):
        """ Runs the command. Overridden from the super-class.
        """

        listing = os.listdir(self.config_dir)
        if listing:
            msg = '{0} is not empty. Please re-run the command in an empty directory.\n'
            msg = msg.format(self.config_dir)
            self._error(msg, False)

        config_py_template = self.app_ctx.get_object('config_py_template')
        config_py_template = config_py_template.format(INSTANCE_SECRET=uuid.uuid4().hex,
                                                       INSTANCE_UNIQUE=uuid.uuid4().hex)

        open(os.path.join(self.config_dir, 'config.py'), 'w').write(config_py_template)
        os.mkdir(os.path.join(self.config_dir, 'logs'))

        open(os.path.join(self.config_dir, self._config_marker), 'w').close()

class Start(_Command):
    """ Handles the 'sec-wall --start /path/to/config/dir' command.
    """
    def prepare_config(self):
        allowed_types = ('http', 'https')

        if self.config_mod.server_type not in allowed_types:
            msg = "server_type must be one of {0}, not '{1}'".format(
                allowed_types, self.config_mod.server_type)
            self._error(msg)

        missing = []
        if self.config_mod.server_type == 'https':
            is_https = 1
            for name in('keyfile', 'certfile', 'ca_certs'):
                path = getattr(self.config_mod, name)
                path = os.path.normpath(path)
                if not os.path.exists(path):
                    missing.append(path)
        else:
            is_https = 0

        if missing:
            noun, verb = ('file', 'exists') if len(missing) == 1 else \
                ('files', 'exist')

            msg = "Either set 'start_https' to False"
            msg += ' in {0}'.format(os.path.join(self.config_dir, 'config.py'))
            msg += ' or make sure the following {0} {1}:\n'.format(noun, verb)

            for path in missing:
                msg += '  * {0}\n'.format(path)

            self._error(msg)
        else:
            # Prepare the zdaemon's config for proxy.
            zdaemon_conf = self.app_ctx.get_object('zdaemon_conf_proxy_template')
            zdaemon_conf = zdaemon_conf.format(config_dir=self.config_dir,
                                               is_https=is_https)
            zdaemon_conf_file = os.path.join(self.config_dir, 'zdaemon.conf')
            open(zdaemon_conf_file, 'w').write(zdaemon_conf)
            
            return zdaemon_conf_file

    def run(self, run_zdaemon=True):
        """ Runs the command. Overridden from the super-class.
        """
        # Prepare the config.
        zdaemon_conf_file = self.prepare_config()


        # Start the proxy.
        self._zdaemon_command('start', zdaemon_conf_file)

class Fork(_Command):
    """ Handles the 'sec-wall --fork /path/to/config/dir is_https' command.
    """

    def run(self):
        """ Configures logging and runs the command. Overridden from the super-class.
        """
        log_file_config = self.config_mod.log_file_config

        if log_file_config:
            logging.config.fileConfig(log_file_config)
        else:
            syslog_facility = self.config_mod.syslog_facility
            log_level = self.config_mod.log_level
            syslog_address = self.config_mod.syslog_address

            log_level = logging.getLevelName(log_level)

            handler = SysLogHandler(syslog_address, syslog_facility)
            handler.setFormatter(LoggingFormatter())

            logger = logging.getLogger('')
            logger.addHandler(handler)
            logger.setLevel(log_level)

        object_name = 'https_proxy_class' if self.is_https else 'http_proxy_class'

        proxy_class = self.app_ctx.get_object(object_name)
        proxy_class(self.config_mod, self.app_ctx).serve_forever()

class Stop(_Command):
    """ Handles the 'sec-wall --stop /path/to/config/dir' command.
    """
    needs_config_mod = False

    def run(self):
        """ Runs the command. Overridden from the super-class.
        """

        zdaemon_conf = os.path.join(self.config_dir, 'zdaemon.conf')
        if not os.path.exists(zdaemon_conf):
            msg = 'No sec-wall processes are running in {0}.\n'.format(self.config_dir)
            self._error(msg, False)

        self._zdaemon_command('stop', zdaemon_conf)

def prepare_config(target_dir, is_https):
    app_ctx = ApplicationContext(app_context.SecWallContext())
    start = Start(target_dir, app_ctx, is_https)
    start.prepare_config()
