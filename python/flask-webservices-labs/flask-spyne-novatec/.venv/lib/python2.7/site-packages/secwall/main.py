# -*- coding: utf-8 -*-

"""
Copyright (C) 2010 Dariusz Suchojad <dsuch at gefira.pl>

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

# gevent
import gevent.monkey
gevent.monkey.patch_all()

# stdlib
import argparse, os, sys

# Spring Python
from springpython.context import ApplicationContext

# sec-wall
from secwall import app_context, cli
from secwall.core import version

description = 'sec-wall {0}- A feature packed security proxy'.format(version)

init_help = 'Initializes a config directory'
start_help = 'Starts sec-wall in the given directory'
stop_help = 'Stops a sec-wall instance running in the given directory'
fork_help = 'Starts one of the sec-wall\'s subprocesses'

class MyFormatter(argparse.ArgumentDefaultsHelpFormatter):
    """ A nicer help formatter, setting 'max_help_position' to that value
    ensures the help doesn't span multiple lines in an awkward way.
    """
    max_help_position = 35

    def __init__(self, **kwargs):
        super(MyFormatter, self).__init__(max_help_position=self.max_help_position,
                                          **kwargs)

    def _get_help_string(self, action):
        """ Overridden from the super-class to prevent showing of defaults,
        as there are no default values.
        """
        return action.help

def get_parser():
    """ Returns an argparse.ArgumentParser instance for parsing the command line
    arguments.
    """
    parser = argparse.ArgumentParser(prog='sec-wall', description=description,
                                     formatter_class=MyFormatter)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--init', help=init_help)
    group.add_argument('--start', help=start_help)
    group.add_argument('--stop', help=stop_help)

    return parser

def handle_fork(argv):
    """ Parses sys.argv when the --fork command has been requested.
    """
    is_https = argv[-1]
    fork_idx = argv.index('--fork')
    config_dir = os.path.abspath(os.path.sep.join(argv[fork_idx+1:-1]))

    return 'fork', [config_dir, is_https]

def run():

    # Special-case the --fork option so that it doesn't get exposed to users.
    # The idea is that --fork is an internal detail which shouldn't be visible
    # anywhere.
    if '--fork' in sys.argv:
        command, config_info = handle_fork(sys.argv)
    else:
        parser = get_parser()
        args = parser.parse_args()

        # Using a mutually exclusive group in 'get_parser' gurantees that we'll have
        # exactly one option to pick here.
        command, config_info = [(k, v) for k, v in args._get_kwargs() if v][0]

    if command == 'fork':
        config_dir, is_https = config_info
    else:
        config_dir = config_info
        is_https = None

    config_dir = os.path.abspath(config_dir)

    app_ctx = ApplicationContext(app_context.SecWallContext())

    handler_class = getattr(cli, command.capitalize())
    handler_class(config_dir, app_ctx, is_https).run()

if __name__ == '__main__':
    run()
