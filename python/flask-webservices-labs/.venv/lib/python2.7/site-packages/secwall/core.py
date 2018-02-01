# -*- coding: utf-8 -*-

"""
Copyright (C) 2010 Dariusz Suchojad <dsuch at gefira.pl>

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

# stdlib
import logging
from datetime import timedelta

# PyYAML
from yaml import dump
try:
    from yaml import CDumper as Dumper
except ImportError:                      # pragma: no cover
    from yaml import Dumper              # pragma: no cover

version_info = ('1', '1')
version = '.'.join(version_info)

class SecWallException(Exception):
    """ A base class for any exception raised by sec-wall
    """

class SecurityException(SecWallException):
    """ Indicates problems with validating incoming requests. The 'description'
    attribute holds textual information suitable for showing to human users.
    """
    def __init__(self, description):
        self.description = description

class AuthResult(object):
    """ Represents the result of validating a URL against the config. 'status'
    is the main boolean flag indicating whether the successful was successful
    or not. 'code' equal to '0' means success and any other value
    is a failure, note that 'code' may be a multi-character string including
    punctuation. 'description' is an optional attribute holding any additional
    textual information a callee might wish to pass to the calling layer.
    'auth_info' is either an empty string or information regarding the authorization
    data presented by the calling application.

    Instances of this class are considered True or False in boolean comparisons
    according to the boolean value of self.status.
    """
    def __init__(self, status=False, code='-1', description=''):
        self.status = status
        self.code = code
        self.description = description
        self._auth_info = b''

    @property
    def auth_info(self):
        return self._auth_info

    @auth_info.setter
    def auth_info(self, value):
        self._auth_info = dump(value, Dumper=Dumper)

    def __repr__(self):
        return '<{0} at {1} status={2} code={3} description={4} auth_info={5}>'.format(
            self.__class__.__name__, hex(id(self)), self.status, self.code,
            self.description, self.auth_info)

    def __nonzero__(self):
        """ Returns the boolean value of self.status. Useful when an instance
        must be compared in a boolean context.
        """
        return bool(self.status)

class LoggingFormatter(logging.Formatter):
    """ A custom logging formatter which prepends every message emitted
    with the string 'sec-wall'.
    """
    def format(self, record):
        message = logging.Formatter.format(self, record)
        return 'sec-wall {0}'.format(message)

class InvocationContext(object):
    """ Contains meta-data describing the given invocation of a proxy
    by the client application.

    - 'instance_name' taken from the config.
    - 'instance_unique' is the same as INSTANCE_UNIQUE in the config.
    - 'message_number' is the next consecutive integer assigned to the given
      invocation.
    - 'proc_start' is the time the request got passed to sec-wall
      (not including time spent in gevent).
    - 'proc_end' is the time request left sec-wall.
    - 'ext_start' is the time the external backend application has been invoked.
    - 'ext_end' is the time the external application returned the response to sec-wall.
    - 'invocation_id' is a unique identifier assigned to a given invocation.
    """
    def __init__(self, instance_name=None, instance_unique=None, message_number=None,
                 proc_start=None, proc_end=None, ext_start=timedelta(), ext_end=timedelta(),
                 env=None, url_config={}, client_cert=None, data='',
                 remote_address=None, auth_result=None, config_type='', path_info=None,
                 query_string=None, client_address=None, request_method=None,
                 client_cert_der=None):
        self.instance_name = instance_name
        self.instance_unique = instance_unique
        self.message_number = message_number
        self.proc_start = proc_start
        self.proc_end = proc_end
        self.ext_start = ext_start
        self.ext_end = ext_end
        self.env = env
        self.url_config = url_config
        self.client_cert = client_cert
        self.data = data
        self.remote_address = remote_address
        self.auth_result = auth_result
        self.config_type = config_type
        self.path_info = path_info
        self.query_string = query_string
        self.client_address = client_address
        self.request_method = request_method
        self.stop_watch_format = '{0.seconds}.{0.microseconds:06d}'
        self.invocation_id = '{0}/{1}/{2}'.format(instance_name, instance_unique, message_number)
        self.invocation_id_signed = ''
        self.client_cert_der = client_cert_der

    def format_log_message(self, code, needs_details):
        """ Returns a nicely formatted log message. Amount of information
        returned depends on the log_level, the higher it is (on a scale where
        ERROR is considered lower than DEBUG) the more information is being
        returned.
        """

        # First batch of information is always returned regardless of the logging level.

        proc_total = self.proc_end - self.proc_start
        ext_overhead = self.ext_end - self.ext_start
        secwall_overhead = proc_total - ext_overhead

        s = '{0};{1};{2};{3};{4} {5}{6};{7};{8};{9};{10};{11}'.format(
                self.invocation_id, code,
                self.proc_start, self.remote_address,
                self.request_method, self.path_info,
                self.query_string,
                self.stop_watch_format.format(secwall_overhead),
                self.stop_watch_format.format(ext_overhead),
                self.stop_watch_format.format(proc_total),
                (0 if self.auth_result else 1),
                self.auth_result.code
            )

        if needs_details:
            s += ';"{0}";{1};{2};{3};{4};{5}'.format(
                self.env.get('HTTP_USER_AGENT'), self.env.get('SERVER_SOFTWARE'),
                self.env.get('SERVER_NAME'), self.env.get('SERVER_PORT'),
                self.config_type, self.data or '')

        return s
