# -*- coding: utf-8 -*-

"""
Copyright (C) 2010 Dariusz Suchojad <dsuch at gefira.pl>

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

# stdlib
import hashlib, itertools, logging, re, ssl, sys, time, traceback, urllib2, uuid
from base64 import b64encode
from datetime import datetime
from urllib import quote_plus, quote

# lxml
from lxml import etree

# gevent
from gevent import pywsgi, sleep, wsgi
from gevent.hub import GreenletExit

# pesto
from pesto.dispatch import ExtensiblePattern

# sec-wall
from secwall import wsse
from secwall.constants import *
from secwall.core import AuthResult, InvocationContext, SecurityException, SecWallException

def on_ssl_cert(url_config, client_cert, field_prefix, needs_auth_info=True):
    """ Visit _RequestApp._on_ssl_cert method's docstring.
    """
    if client_cert:
        config_fields = {}
        for field, value in url_config.items():
            if field.startswith(field_prefix):
                config_fields[field.split(field_prefix)[1]] = value

        # There are no fields so the user just wants the connection be
        # encrypted and the client use client certificate however they're
        # not interested in the cert's fields - so as long as the CA is
        # OK (and we know it is because otherwise we wouldn't have gotten
        # so far), we let the client in.
        if not config_fields:
            return True
        else:
            subject =  client_cert.get('subject')
            if not subject:
                return AuthResult(False, AUTH_CERT_NO_SUBJECT)

            cert_fields = dict((elem[0][0].encode('utf-8'), elem[0][1].encode('utf-8')) for elem in subject)
            
            for config_field, config_value in config_fields.items():
                cert_value = cert_fields.get(config_field)
                if not cert_value:
                    return AuthResult(False, AUTH_CERT_NO_VALUE)
                if cert_value != config_value:
                    return AuthResult(False, AUTH_CERT_VALUE_MISMATCH)
            else:
                auth_result = AuthResult(True, '0')
                if needs_auth_info:
                    auth_result.auth_info = dict((quote_plus(k), quote_plus(v)) for k, v in cert_fields.iteritems())

                return auth_result

def on_wsse_pwd(wsse, url_config, data, needs_auth_info=True):
    """ Visit _RequestApp._on_wsse_pwd method's docstring.
    """
    if not data:
        return AuthResult(False, AUTH_WSSE_NO_DATA)

    request = etree.fromstring(data)
    try:
        ok, wsse_username = wsse.validate(request, url_config)
    except SecurityException, e:
        return AuthResult(False, AUTH_WSSE_VALIDATION_ERROR, e.description)
    else:
        auth_result = AuthResult(True, '0')
        if needs_auth_info:
            auth_result.auth_info = {b'wsse-pwd-username': str(wsse_username)}

        return auth_result
        
def _on_basic_auth(auth, expected_username, expected_password):
    """ A low-level call for checking the HTTP Basic Auth credentials.
    """
    if not auth:
        return AUTH_BASIC_NO_AUTH

    prefix = 'Basic '
    if not auth.startswith(prefix):
        return AUTH_BASIC_INVALID_PREFIX

    _, auth = auth.split(prefix)
    auth = auth.strip().decode('base64')

    username, password = auth.split(':', 1)

    if username == expected_username and password == expected_password:
        return True
    else:
        return AUTH_BASIC_USERNAME_OR_PASSWORD_MISMATCH

def on_basic_auth(env, url_config, needs_auth_info=True):
    """ Visit _RequestApp._on_basic_auth method's docstring.
    """
    username = url_config['basic-auth-username']
    result = _on_basic_auth(env.get('HTTP_AUTHORIZATION', ''), username, url_config['basic-auth-password'])
    is_success = result is True # Yes, need to check for True
    
    auth_result = AuthResult(is_success)
        
    if is_success: 
        if needs_auth_info:
            auth_result.auth_info = {b'basic-auth-username': quote_plus(username).encode('utf-8')}
    else:
        auth_result.code = result
        
    return auth_result

class _RequestApp(object):
    """ A WSGI application executed on each request.
    """
    def __init__(self, config=None, app_ctx=None):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.config = config
        self.urls = []
        self.app_ctx = app_ctx
        self.wsse = self.app_ctx.get_object('wsse')

        self.server_tag = config.server_tag
        self.instance_name = config.instance_name
        self.instance_unique = config.INSTANCE_UNIQUE
        self.instance_secret = config.INSTANCE_SECRET
        self.quote_path_info = config.quote_path_info
        self.quote_query_string = config.quote_query_string
        self.from_backend_ignore  = config.from_backend_ignore
        self.add_invocation_id = config.add_invocation_id
        self.sign_invocation_id = config.sign_invocation_id
        self.add_default_if_not_found = config.add_default_if_not_found

        self.msg_counter = itertools.count(1)
        self.now = datetime.now
        self.log_level = self.logger.getEffectiveLevel()

        seen_default = False
        default_pattern = ExtensiblePattern("<default:path>")

        for url_pattern, url_config in self.config.urls:
            if url_pattern == '/*':
                self.urls.append((default_pattern, url_config))
                seen_default = True

            self.urls.append((ExtensiblePattern(url_pattern), url_config))

            url_config.setdefault('from-client-ignore', [])
            url_config.setdefault('to-backend-add', {})
            url_config.setdefault('from-backend-ignore', config.from_backend_ignore)
            url_config.setdefault('to-client-add', {})

            # Just in case the user didn't do it, upper-case all the headers
            # to make all the comparisons case-insensitive.
            url_config['from-client-ignore'][:] = map(str.upper, url_config.get('from-client-ignore', {}))

        if not seen_default and self.add_default_if_not_found:
            self.urls.append((default_pattern, self.config.default_url_config))

    def __call__(self, env, start_response, client_cert=None, client_cert_der=None):
        """ Finds the configuration for the given URL and passes the control on
        to the main request handler. In case no config for the given URL is
        found, a 404 Not Found will be returned to the calling side.
        """
        ctx = InvocationContext(self.instance_name, self.instance_unique, self.msg_counter.next(),
                                self.now())
        ctx.auth_result = AuthResult()
        ctx.env = env

        ctx.client_cert = client_cert
        ctx.client_cert_der = client_cert_der

        if self.sign_invocation_id:
            h = hashlib.sha256()
            h.update('{0}:{1}'.format(self.instance_secret, ctx.invocation_id))
            ctx.invocation_id_signed = h.hexdigest()

        path_info = env['PATH_INFO']
        if self.quote_path_info:
            path_info = quote_plus(path_info)

        query_string = env.get('QUERY_STRING')
        if query_string:
            query_string = '?' + query_string
            if self.quote_query_string:
                query_string = quote_plus(query_string)

        ctx.path_info = path_info
        ctx.query_string = query_string
        ctx.remote_address = env.get('REMOTE_ADDR')
        ctx.request_method = env.get('REQUEST_METHOD')

        for c, url_config in self.urls:
            match = c.test(path_info)
            if match:
                ctx.url_config = url_config
                return self._on_request(ctx, start_response, env, url_config,
                                        client_cert, match)
        else:
            # No config for that URL, we can't let the client in.
            return self._404(ctx, start_response)

    def _on_request(self, ctx, start_response, env, url_config, client_cert, match=None):
        """ Checks security, invokes the backend server, returns the response.
        """

        # If True, we know we're being accessed using SSL.
        has_ssl = False

        # Some quick SSL-related checks first.
        if url_config.get('ssl'):

            # Has the URL been accessed through SSL/TLS?
            if env.get('wsgi.url_scheme') != 'https':
                return self._403(ctx, start_response)

            # OK, we're now sure we're being invoked through SSL.
            has_ssl = True

            # Is the client cert required?
            if url_config.get('ssl-cert') and not client_cert:
                return self._401(ctx, start_response, self._get_www_auth(url_config, 'ssl-cert'))

        data = env['wsgi.input'].read()
        data = data if data else None
        ctx.data = data

        # ssl-wrap-only implies 'ssl':True but everyone's free to forget about
        # setting it so we may wind up ostensibly using SSL yet in reality
        # we'd be using plain HTTP. That's why there's an additional check
        # for 'has_ssl' below.
        if url_config.get('ssl-wrap-only'):
            if not has_ssl:
                return self._403(ctx, start_response)
            else:
                # There will be no authentication performed and we need to fill
                # in the information ourselves here so that what goes to logs
                # doesn't use the ctx's defaults.
                ctx.auth_result = AuthResult(True, '0')
        else:
            for config_type in self.config.validation_precedence:
                if config_type in url_config:

                    handler = getattr(self, '_on_' + config_type.replace('-', '_'))
                    auth_result = handler(env, url_config, client_cert, data)

                    ctx.auth_result = auth_result
                    ctx.config_type = config_type

                    if not auth_result:
                        return self._401(ctx, start_response, self._get_www_auth(url_config, config_type))
                    break
            else:
                return self._500(ctx, start_response)

        rewrite = url_config.get('rewrite')
        if rewrite:
            path_info = rewrite.format(**match[1])
        else:
            path_info = env['PATH_INFO']

        req = urllib2.Request(url_config['host'] + path_info, data)

        from_client_ignore = url_config['from-client-ignore']
        to_backend_add = url_config['to-backend-add']

        # Pass the headers to the backend server unless they're to be ignored.
        for name in (name for name in env if name.startswith('HTTP_')):
            value = env[name]
            name = name.split('HTTP_')[1].replace('_', '-')
            if not name in from_client_ignore:
                req.add_header(name, value)

        # Custom headers to be sent to the backend server.
        for name, value in to_backend_add.iteritems():
            req.add_header(name, value)

        # Sign and return the invocation ID.
        if self.add_invocation_id:
            req.add_header('X-sec-wall-invocation-id', ctx.invocation_id)

        if self.sign_invocation_id:
            req.add_header('X-sec-wall-invocation-id-signed', ctx.invocation_id_signed)

        if url_config.get('add-auth-info', True):
            req.add_header('X-sec-wall-auth-info', ctx.auth_result.auth_info.strip())

        if url_config.get('sign-auth-info', True):
            h = hashlib.sha256()
            h.update('{0}:{1}:{2}'.format(ctx.invocation_id, self.instance_secret,
                                          ctx.auth_result.auth_info.strip()))
            req.add_header('X-sec-wall-auth-info-signed', h.hexdigest())

        try:
            opener = urllib2.build_opener()
            ctx.ext_start = self.now()
            resp = opener.open(req)
        except urllib2.HTTPError, e:
            resp = e
        try:
            response = resp.read()
            resp.close()
        finally:
            ctx.ext_end = self.now()

        return self._response(ctx, start_response, str(resp.getcode()), resp.msg,
                              resp.headers.dict, response)

    def _response(self, ctx, start_response, code, status, headers, response):
        """ Actually returns the response to the client.
        """
        # We need details in case there was an error or we're running
        # at least on DEBUG level.
        if ctx.auth_result.status is False:
            needs_details = True
        elif self.log_level <= logging.DEBUG:
            needs_details = True
        else:
            needs_details = False

        if ctx.url_config:
            for name in ctx.url_config['from-backend-ignore']:
                headers.pop(name, None)

            headers.update(ctx.url_config['to-client-add'])
        else:
            # Special-case the 'Server' header.
            if 'Server' in self.from_backend_ignore:
                headers['Server'] = self.server_tag

        # Sign and return the invocation ID.
        if self.add_invocation_id:
            headers['X-sec-wall-invocation-id'] = ctx.invocation_id

        if self.sign_invocation_id:
            headers['X-sec-wall-invocation-id-signed'] = ctx.invocation_id_signed

        ctx.proc_end = self.now()
        log_message = ctx.format_log_message(code, needs_details)

        if ctx.auth_result:
            self.logger.info(log_message)
        else:
            self.logger.error(log_message)

        start_response('{0} {1}'.format(code, status), headers.items())
        return [response]

    def _get_www_auth(self, url_config, config_type):
        """ Returns a value of the WWW-Authenticate header to use upon a 401 error.
        """
        www_auth = {
            'ssl-cert': self.config.client_cert_401_www_auth,
            'basic-auth': 'Basic realm="{realm}"',
            'digest-auth': 'Digest realm="{realm}", nonce="{nonce}", opaque="{opaque}"',
            'wsse-pwd': 'WSSE realm="{realm}", profile="UsernameToken"',
            'custom-http': 'custom-http',
            'xpath': 'xpath'
        }
        header_value = www_auth[config_type]

        if config_type in('basic-auth', 'wsse-pwd'):
            header_value = header_value.format(realm=url_config[config_type + '-realm'])
        elif config_type == 'digest-auth':
            realm = url_config['digest-auth-realm']
            nonce = uuid.uuid4().hex
            opaque = uuid.uuid4().hex

            header_value = header_value.format(realm=realm, nonce=nonce, opaque=opaque)

        return header_value

    def _401(self, ctx, start_response, www_auth):
        """ 401 Not Authorized
        """
        code, status, content_type, description = self.config.not_authorized
        headers = {'Content-Type':content_type, 'WWW-Authenticate':www_auth}

        return self._response(ctx, start_response, code, status, headers, description)

    def _403(self, ctx, start_response):
        """ 403 Forbidden
        """
        code, status, content_type, description = self.config.forbidden
        return self._response(ctx, start_response, code, status, {'Content-Type':content_type}, description)

    def _404(self, ctx, start_response):
        """ 404 Not Found
        """
        code, status, content_type, description = self.config.no_url_match
        return self._response(ctx, start_response, code, status, {'Content-Type':content_type}, description)

    def _500(self, ctx, start_response):
        """ 500 Internal Server Error
        """
        code, status, content_type, description = self.config.internal_server_error
        return self._response(ctx, start_response, code, status, {'Content-Type':content_type}, description)

    def _on_ssl_cert(self, env, url_config, client_cert, data, field_prefix='ssl-cert-'):
        """ Validates the client SSL/TLS certificates, its very existence and
        the values of its fields (commonName, organizationName etc.)
        """
        return on_ssl_cert(url_config, client_cert, field_prefix)

    def _on_wsse_pwd(self, env, url_config, unused_client_cert, data):
        """ Uses WS-Security UsernameToken/Password to validate the request.
        """
        return on_wsse_pwd(self.wsse, url_config, data)

    def _on_basic_auth(self, env, url_config, *ignored):
        """ Handles HTTP Basic Authentication.
        """
        return on_basic_auth(env, url_config)

    def _parse_digest_auth(self, auth):
        """ Parses the client's Authorization header and transforms it into
        a dictionary.
        """
        out = {}
        auth = auth.replace('Digest ', '', 1).split(',')
        for item in auth:
            key, value = item.split('=', 1)
            key = key.strip()
            value = value[1:-1] # Strip quotation marks
            out[key] = value
        return out

    def _compute_digest_auth_response(self, expected_username, expected_realm,
                    expected_password, expected_uri, request_method, nonce):
        """ Returns the Digest Auth response as understood by RFC 2069.
        """

        # HA1
        ha1 = hashlib.md5()
        ha1.update('{0}:{1}:{2}'.format(expected_username, expected_realm, expected_password))

        # HA2
        ha2 = hashlib.md5()
        ha2.update('{0}:{1}'.format(request_method, expected_uri))

        # response
        respone = hashlib.md5()
        respone.update('{0}:{1}:{2}'.format(ha1.hexdigest(), nonce, ha2.hexdigest()))

        return respone.hexdigest()

    def _on_digest_auth(self, env, url_config, *ignored):
        """ Handles HTTP Digest Authentication.
        """
        auth = env.get('HTTP_AUTHORIZATION')
        if not auth:
            return AuthResult(False, AUTH_DIGEST_NO_AUTH)

        auth = self._parse_digest_auth(auth)

        expected_username = url_config['digest-auth-username']
        expected_password = url_config['digest-auth-password']
        expected_realm = url_config['digest-auth-realm']

        if auth['username'] != expected_username:
            return AuthResult(False, AUTH_DIGEST_USERNAME_MISMATCH)

        if auth['realm'] != expected_realm:
            return AuthResult(False, AUTH_DIGEST_REALM_MISMATCH)

        if env.get('QUERY_STRING'):
            expected_uri = '{0}?{1}'.format(env['PATH_INFO'], env['QUERY_STRING'])
        else:
            expected_uri = env['PATH_INFO']

        if auth['uri'] != expected_uri:
            return AuthResult(False, AUTH_DIGEST_URI_MISMATCH)

        expected_response = self._compute_digest_auth_response(expected_username,
                                expected_realm, expected_password, expected_uri,
                                env['REQUEST_METHOD'], auth['nonce'])

        if auth['response'] == expected_response:
            auth_result = AuthResult(True, '0')
            auth_result._auth_info = {b'digest-auth-username':quote_plus(expected_username),
                                      b'digest-auth-realm':quote_plus(expected_realm)}

            return auth_result
        else:
            return AuthResult(False, AUTH_DIGEST_RESPONSE_MISMATCH)

    def _on_custom_http(self, env, url_config, *ignored):
        """ Handles the authentication based on custom HTTP headers.
        """
        prefix = 'custom-http-'

        expected_headers = {}
        expected_headers_keys = (header for header in url_config if header.startswith(prefix))

        for key in expected_headers_keys:
            # This set of operations (.split, .upper, .replace) could be done once
            # when the config's read, well, it's a room for improvement.
            expected_headers[str(key)] = str(env.get('HTTP_' + key.split(prefix)[1].upper().replace('-', '_'), ''))

        if not expected_headers:

            # It's clearly an error. We've been requested to use custom HTTP
            # headers but none are in the config.
            raise SecWallException('No custom HTTP headers were found in the config')

        for key, value in expected_headers.iteritems():
            if not value:
                return AuthResult(False, AUTH_CUSTOM_HTTP_NO_HEADER)

            if value != url_config[key]:
                return AuthResult(False, AUTH_CUSTOM_HTTP_HEADER_MISMATCH)
        else:
            auth_result = AuthResult(True, '0')
            auth_result.auth_info = expected_headers

            return auth_result

    def _on_xpath(self, unused_env, url_config, unused_client_cert, data):
        """ Handles the authentication based on XPath expressions.
        """
        if not data:
            return AuthResult(False, AUTH_XPATH_NO_DATA)

        request = etree.fromstring(data)

        prefix = 'xpath-'
        expressions = [url_config[header] for header in url_config if header.startswith(prefix)]

        if not expressions:

            # It's clearly an error. We've been requested to use XPath yet no
            # expressions have been defined in the config.
            raise SecWallException('No XPath expressions were found in the config')

        for expr in expressions:
            if not expr(request):
                return AuthResult(False, AUTH_XPATH_EXPR_MISMATCH)
        else:
            auth_result = AuthResult(True, '0')
            auth_result.auth_info = map(str, expressions)

            return auth_result

class _RequestHandler(pywsgi.WSGIHandler):
    """ A subclass which conveniently exposes a client SSL/TLS certificate
    to the layers above. Note that some of the lines have been given the
    '# pragma: no cover' comment, that's because they were simply copy & pasted
    from the base class and we have no tests to cover them.
    """
    def handle_one_response(self):
        self.time_start = time.time()
        self.status = None
        self.headers_sent = False

        self.result = None
        self.response_use_chunked = False
        self.response_length = 0

        try:
            try:
                if hasattr(self.socket, 'getpeercert'):
                    cert = self.socket.getpeercert()
                    cert_der = self.socket.getpeercert(True)
                else:
                    cert = None
                    cert_der = None
                self.result = self.application(self.environ, self.start_response, cert, cert_der)
                for data in self.result:
                    if data:
                        self.write(data)
                if self.status and not self.headers_sent:
                    self.write('')                               # pragma: no cover
                if self.response_use_chunked:                    # pragma: no cover
                    self.wfile.writelines('0\r\n\r\n')           # pragma: no cover
                    self.response_length += 5                    # pragma: no cover
            except GreenletExit:                                 # pragma: no cover
                raise                                            # pragma: no cover
            except Exception:                                    # pragma: no cover
                traceback.print_exc()                            # pragma: no cover
                sys.exc_clear()                                  # pragma: no cover
                try:                                             # pragma: no cover
                    args = (getattr(self, 'server', ''),         # pragma: no cover
                            getattr(self, 'requestline', ''),    # pragma: no cover
                            getattr(self, 'client_address', ''), # pragma: no cover
                            getattr(self, 'application', ''))    # pragma: no cover
                    msg = '%s: Failed to handle request:\n  request = %s from %s\n  application = %s\n\n' % args # pragma: no cover
                    sys.stderr.write(msg)                        # pragma: no cover
                except Exception:                                # pragma: no cover
                    sys.exc_clear()                              # pragma: no cover
                if not self.response_length:                     # pragma: no cover
                    self.start_response(pywsgi._INTERNAL_ERROR_STATUS, pywsgi._INTERNAL_ERROR_HEADERS) # pragma: no cover
                    self.write(pywsgi._INTERNAL_ERROR_BODY)      # pragma: no cover
        finally:                                                 # pragma: no cover
            if hasattr(self.result, 'close'):                    # pragma: no cover
                self.result.close()                              # pragma: no cover
            self.wsgi_input._discard()
            self.time_finish = time.time()
            self.log_request()

class HTTPProxy(wsgi.WSGIServer):
    """ A plain HTTP proxy.
    """
    def __init__(self, config, app_ctx):
        self.logger = logging.getLogger(self.__class__.__name__)
        wsgi_request_app = app_ctx.get_object('wsgi_request_app')

        super(HTTPProxy, self).__init__((config.host, config.port),
                wsgi_request_app(config, app_ctx), log=config.log)

class HTTPSProxy(pywsgi.WSGIServer):
    """ An SSL/TLS proxy.
    """
    def __init__(self, config, app_ctx):
        self.logger = logging.getLogger(self.__class__.__name__)
        wsgi_request_app = app_ctx.get_object('wsgi_request_app')
        wsgi_request_handler = app_ctx.get_object('wsgi_request_handler')

        super(HTTPSProxy, self).__init__((config.host, config.port),
                wsgi_request_app(config, app_ctx), log=config.log,
                handler_class=wsgi_request_handler, keyfile=config.keyfile,
                certfile=config.certfile, ca_certs=config.ca_certs,
                cert_reqs=ssl.CERT_OPTIONAL)

    def handle(self, socket, address):
        handler = self.handler_class(socket, address, self)
        handler.handle()
