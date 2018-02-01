# -*- coding: utf-8 -*-

"""
Copyright (C) 2010 Dariusz Suchojad <dsuch at gefira.pl>

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

# stdlib
import multiprocessing, os.path as path
from logging.handlers import SysLogHandler
from uuid import uuid4

# Spring Python
from springpython.config import Object, PythonConfig
from springpython.context import scope

# sec-wall
from secwall import server, wsse
from secwall.core import version

class SecWallContext(PythonConfig):
    """ A Spring Python's application context for sec-wall.
    """

    @Object
    def http_proxy_class(self):
        """ Instances of this class will be handling HTTP traffic.
        """
        return server.HTTPProxy

    @Object
    def https_proxy_class(self):
        """ Instances of this class will be handling HTTPS traffic.
        """
        return server.HTTPSProxy

    @Object
    def wsgi_request_handler(self):
        """ Instances of this class reimplement gevent.pywsgi.WSGIHandler.handle_one_response
        method for the purpose of adding the support for client SSL/TLS certs.
        """
        return server._RequestHandler

    @Object
    def wsgi_request_app(self):
        """ The main WSGI application whose __call__ method - called on
        each request - will be responsible for the processing of an incoming
        request.
        """
        return server._RequestApp

    @Object
    def wsse(self):
        return wsse.WSSE()

    @Object
    def server_type(self):
        """ Whether to start a plain HTTP (http) server or an SSL/TLS one (https).
        Defaults to 'http'.
        """
        return 'http'

    @Object
    def host(self):
        """ Host to bind to.
        """
        return '0.0.0.0'

    @Object
    def port(self):
        """ Port to bind to.
        """
        return 15100

    @Object
    def log(self):
        """ Whether to log plain HTTP traffic.
        """
        return False

    @Object
    def crypto_dir(self):
        """ The base directory holding crypto material.
        """
        return './crypto'

    @Object
    def keyfile(self):
        """ Location of the server's private key.
        """
        return path.join(self.crypto_dir(), 'server-priv.pem')

    @Object
    def certfile(self):
        """ Location of the server's certificate.
        """
        return path.join(self.crypto_dir(), 'server-cert.pem')

    @Object
    def ca_certs(self):
        """ Location of the file containing CAs the server is to trust.
        """
        return path.join(self.crypto_dir(), 'ca-cert.pem')

    @Object
    def not_authorized(self):
        """ HTTP code, the content type and a user friendly description
        for 401 error.
        """
        return ['401', 'Not Authorized', 'text/plain', str('You are not authorized to access this resource')]

    @Object
    def forbidden(self):
        """ HTTP code, the content type and a user friendly description
        for 403 error.
        """
        return ['403', 'Forbidden', 'text/plain', str('You are not allowed to access this resource')]

    @Object
    def no_url_match(self):
        """ HTTP code, the content type and a user friendly description
        for 404 error.
        """
        return ['404', 'Not Found', 'text/plain', str('Not Found')]

    @Object
    def internal_server_error(self):
        """ HTTP code, the content type and a user friendly description
        for 500 error.
        """
        return ['500', 'Internal Server Error', 'text/plain', str('Internal Server Error')]

    @Object
    def validation_precedence(self):
        """ The order of types of security configuration. If there's more than
        one configuration for the given URL, only one will be used and it will
        the one that is higher on this list (closer to index 0).
        """
        return ['ssl-cert', 'basic-auth', 'digest-auth', 'wsse-pwd', 'custom-http', 'xpath']

    @Object
    def client_cert_401_www_auth(self):
        """ See disussion at http://www6.ietf.org/mail-archive/web/tls/current/msg05589.html
        """
        return 'Transport mode="tls-client-certificate"'

    @Object
    def syslog_facility(self):
        """ Syslog facility.
        """
        return SysLogHandler.LOG_USER

    @Object
    def syslog_address(self):
        """ Syslog address, should be either b'/dev/log' or the UDP address
        such as ['127.0.0.1', 514].
        """
        return b'/dev/log'

    @Object
    def log_level(self):
        """ The log level to use.
        """
        return 'INFO'

    @Object
    def log_file_config(self):
        """ Path to an external configuration of the logging machinery.
        """
        return None

    @Object
    def server_tag(self):
        """ How will sec-wall introduce itself to client and backend applications
        in HTTP headers.
        """
        return 'sec-wall/{0}'.format(version)

    @Object
    def instance_name(self):
        """ A human-friendly name of this particular sec-wall instance.
        """
        return 'default'

    @Object
    def quote_path_info(self):
        """ Whether to quote PATH_INFO during logging. Set to True when URLs
        may be outside ASCII range.
        """
        return False

    @Object
    def quote_query_string(self):
        """ Whether to quote QUERY_STRING during logging. Set to True when URLs
        may be outside ASCII range.
        """
        return False

    @Object
    def from_backend_ignore(self):
        """ Headers belonging to this list will not be returned to the client
        application even if a backend sends them in.
        """
        return ['Server']

    @Object
    def add_invocation_id(self):
        """ Whether client and backend applications should receive
        the X-sec-wall-invocation-id HTTP header.
        """
        return True

    @Object
    def sign_invocation_id(self):
        """ Whether client and backend applications should receive
        the X-sec-wall-invocation-id-signed HTTP header.
        """
        return True

    @Object
    def default_url_config(self):
        """ The configuration to use for the '/*' URL pattern in case a user
        didn't provide any. Uses lots of random UUIDs to make sure no client
        data will ever match the config, that is, by default no one will be able
        to invoke the URL.
        """
        return {
            'ssl': True,
            'ssl-cert': True,
            'ssl-cert-commonName': uuid4().hex,
            'host': 'http://{0}'.format(uuid4().hex),
            'from-client-ignore': [],
            'to-backend-add': {},
            'from-backend-ignore': [],
            'to-client-add': {}
        }

    @Object
    def add_default_if_not_found(self):
        """ When starting a proxy, whether to add a default configuration for
        a catch-all '/*' pattern if a user-defined configuration for that pattern
        wasn't found.
        """
        return True

    @Object
    def config_py_template(self):
        return """# -*- coding: utf-8 -*-

# stdlib
import os.path as path, uuid

# Don't share it with anyone.
INSTANCE_SECRET = '{INSTANCE_SECRET}'

# May be shared with the outside world.
INSTANCE_UNIQUE = uuid.uuid4().hex

# Useful constants
cur_dir = path.dirname(__file__)

# Crypto
keyfile = path.join(cur_dir, './crypto/server-priv.pem')
certfile = path.join(cur_dir, './crypto/server-cert.pem')
ca_certs = path.join(cur_dir, './crypto/ca-cert.pem')

# ##############################################################################

def default():
    return {{
        'ssl': True,
        'ssl-cert': True,
        'ssl-cert-commonName':INSTANCE_SECRET,
        'host': 'http://' + INSTANCE_SECRET
    }}

urls = [
    ('/*', default()),
]
"""

    @Object
    def zdaemon_conf_proxy_template(self):
        return """
<runner>
    program python -m secwall.main --fork {config_dir} {is_https}
    socket-name {config_dir}/zdaemon.sock
    transcript {config_dir}/logs/proxy.log
</runner>

<eventlog>
    <logfile>
        path {config_dir}/zdaemon.log
    </logfile>
</eventlog>
"""
