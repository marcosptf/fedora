# -*- coding: utf-8 -*-

"""
Copyright (C) 2010 Dariusz Suchojad <dsuch at gefira.pl>

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

# stdlib
import logging, time
from hashlib import sha1
from string import Template
from datetime import datetime, timedelta

# lxml
from lxml import etree

# secwall
from secwall.core import SecurityException

soap_date_time_format = "%Y-%m-%dT%H:%M:%S.%fZ"

soapenv_namespace = 'http://schemas.xmlsoap.org/soap/envelope/'

soap_body_path = '/soapenv:Envelope/soapenv:Body'
soap_body_xpath = etree.XPath(soap_body_path, namespaces={'soapenv':soapenv_namespace})

wsse_namespace = 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd'
wsu_namespace = 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd'

wss_namespaces = {'soapenv':soapenv_namespace, 'wsse':wsse_namespace, 'wsu':wsu_namespace}

wsse_password_type_text = 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText'
wsse_password_type_digest = 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordDigest'

supported_wsse_password_types = (wsse_password_type_text, wsse_password_type_digest)

wsse_username_token_path = '/soapenv:Envelope/soapenv:Header/wsse:Security/wsse:UsernameToken'
wsse_username_token_xpath = etree.XPath(wsse_username_token_path, namespaces=wss_namespaces)

wsse_username_path = '/soapenv:Envelope/soapenv:Header/wsse:Security/wsse:UsernameToken/wsse:Username'
wsse_username_xpath = etree.XPath(wsse_username_path, namespaces=wss_namespaces)

wsse_password_path = '/soapenv:Envelope/soapenv:Header/wsse:Security/wsse:UsernameToken/wsse:Password'
wsse_password_xpath = etree.XPath(wsse_password_path, namespaces=wss_namespaces)

wsse_password_type_path = '/soapenv:Envelope/soapenv:Header/wsse:Security/wsse:UsernameToken/wsse:Password/@Type'
wsse_password_type_xpath = etree.XPath(wsse_password_type_path, namespaces=wss_namespaces)

wsse_nonce_path = '/soapenv:Envelope/soapenv:Header/wsse:Security/wsse:UsernameToken/wsse:Nonce'
wsse_nonce_xpath = etree.XPath(wsse_nonce_path, namespaces=wss_namespaces)

wsu_username_created_path = '/soapenv:Envelope/soapenv:Header/wsse:Security/wsse:UsernameToken/wsu:Created'
wsu_username_created_xpath = etree.XPath(wsu_username_created_path, namespaces=wss_namespaces)

class WSSE(object):
    """ Implements authentication using WS-Security.
    """

    def _replace_username_token_elem(self, soap, old_elem, attr_name):
        """ A utility function for replacing passwords and nonces with '***'
        for the purpose of logging the messages without worrying of disclosing
        any data known to be secret.
        """

        old_elem = old_elem[0]
        attr = old_elem.get(attr_name)

        username_token = wsse_username_token_xpath(soap)
        if not username_token:
            self.error(expected_element=wsse_username_token_path)

        username_token = username_token[0]

        elem_idx = username_token.index(old_elem)
        username_token.remove(old_elem)

        new_elem = etree.Element(old_elem.tag)
        new_elem.set(attr_name, attr)
        new_elem.text = '***'
        username_token.insert(elem_idx, new_elem)

        return old_elem.text, attr

    def _get_digest(self, password, nonce, created):
        """ Returns the password's expected digest.
        """
        nonce = nonce.decode('base64')
        concat = nonce + created + password

        h = sha1()
        h.update(concat)

        return str.encode(h.digest(), 'base64').rstrip('\n')

    def error(self, description='', expected_element='', soap=None):
        """ A utility function for exceptions in erronous situations. May be
        subclassed if error reporting needs to be customized. The 'soap'
        parameter is guaranteed to have WSSE password and token replaced
        with '***' characters. Note that default implementation doesn't use
        the 'soap' parameter however the subclasses are free to do so.
        """
        msg = description
        if expected_element:
            if description:
                msg += '. '
            msg += 'Element [{0}] doesn\'t exist'.format(expected_element)

        raise SecurityException(msg)

    def check_nonce(self, wsse_nonce, now, nonce_freshness_time):
        """ Checks whether the nonce has been already seen. Default implementation
        lets all nonces in. More sophisticated subclasses may wish to override
        this method and check the nonce against a cache of some sort.
        """
        return False

    def on_invalid_username(self, config, given, message):
        """ Invoked when the expected and given usernames don't match.
        """
        self.error('Invalid username or password')

    def on_invalid_password(self, config, given_username, given_password, message):
        """ Invoked when the expected and given passwords don't match.
        """
        self.error('Invalid username or password')

    def on_username_token_expired(self, config, elapsed, message):
        """ Invoked when the username token has been found to be expired.
        """
        self.error('UsernameToken has expired')

    def on_nonce_non_unique(self, config, nonce, now, message):
        """ Invoked when the nonce has been found not to be unique.
        """
        self.error('Nonce [{0}] is not unique'.format(nonce))

    def validate(self, soap, config):

        # Shadow the password and a nonce before any processing, getting
        # their values along the way.

        wsse_password = wsse_password_xpath(soap)
        if wsse_password:
            wsse_password, wsse_password_type = self._replace_username_token_elem(soap, wsse_password, 'Type')

        wsse_nonce = wsse_nonce_xpath(soap)
        if wsse_nonce:
            wsse_nonce, wsse_encoding_type = self._replace_username_token_elem(soap, wsse_nonce, 'EncodingType')

        wsse_username = wsse_username_xpath(soap)
        if not wsse_username:
            self.error('No username sent', wsse_username_path, soap)

        wsse_username = wsse_username[0].text

        if config['wsse-pwd-username'] != wsse_username:
            self.on_invalid_username(config, wsse_username, soap)

        if not wsse_password_type:
            self.error('No password type sent', wsse_password_type_path, soap)

        if not wsse_password_type in supported_wsse_password_types:
            msg = 'Unsupported password type=[{0}], not in [{1}]'.format(wsse_password_type, supported_wsse_password_types)
            self.error(msg, soap=soap)

        now = datetime.utcnow()
        
        if config['wsse-pwd-reject-empty-nonce-creation']:
            
            wsu_username_created = wsu_username_created_xpath(soap)
            if not all((wsse_nonce, wsu_username_created)):
                self.error('Both nonce and creation timestamp must be given', soap=soap)
            else:
                if wsu_username_created:
                    wsu_username_created = wsu_username_created[0].text
    
            # Check nonce freshness and report error if the UsernameToken is stale.
            token_created = datetime.strptime(wsu_username_created, soap_date_time_format)
    
            elapsed = (now - token_created)
    
            if config['wsse-pwd-reject-stale-tokens'] and elapsed.seconds > config['wsse-pwd-reject-expiry-limit']:
                self.on_username_token_expired(config, elapsed, soap)

        if config.get('wsse-pwd-password-digest'):
            expected_password =  self._get_digest(config['wsse-pwd-password'],
                                            wsse_nonce, wsu_username_created)
        else:
            expected_password = config.get('wsse-pwd-password')

        if wsse_password != expected_password:
            self.on_invalid_password(config, wsse_username, wsse_password, soap)

        # Have we already seen such a nonce?
        if self.check_nonce(wsse_nonce, now, config.get('wsse-pwd-nonce-freshness-time')):
            self.on_nonce_non_unique(config, wsse_nonce, now, soap)

        # All good, we let the client in.
        return True, wsse_username
