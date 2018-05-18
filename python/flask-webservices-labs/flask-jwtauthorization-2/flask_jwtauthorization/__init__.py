# Copyright (C) 2017, CERN
# This software is distributed under the terms of the GNU General Public
# Licence version 3 (GPL Version 3), copied verbatim in the file "LICENSE".

# In applying this license, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as Intergovernmental Organization
# or submit itself to any jurisdiction.


from functools import wraps

import jwt
from flask import request, current_app, g, abort


def jwt_authorize(**auth_kwargs):
    """
    This is the decorator to apply to each route you want to protect.
    If you use default parameters, it try to execute a method called
    auth_<verb> within the first parameter passed. This is useful if
    you are using a library like Flask-RESTful.
    In any case, you can specify a class and/or a function to handle
    the authorization.
    You can also pass any additional parameter to the auth function.
    In case of name collision, these parameters will overwrite any
    other defined with the same name in the decorated function.

    :param auth_func:
        asdasdsdasad

        Default: None
    :type auth_func: callable

    :param auth_cls:
        asdasdads

        Default: None
    :type auth_cls: object
    """

    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            token = _token_extractor()
            user = _user_decode(token)
            g.setdefault('user', user)
            auth_func = auth_kwargs.pop('auth_func', None)
            auth_cls = auth_kwargs.pop('auth_cls', None)
            callback = _get_authorization_callback(auth_func, auth_cls, args)
            # jwt_authorize params take preference to Flask route params in case of name collision.
            kwargs.update(auth_kwargs)
            _check_authorization(user, callback, **kwargs)
            return fn(*args, **kwargs)
        return decorator
    return wrapper


def _token_extractor():
    """
    Retrieves the token from the headers.
    There should be an Authorization header with the following format:

        Authorization: <prefix> JWT_TOKEN

    Where <prefix> should be configured in JWTAUTH_BEARER_PREFIX configuration key. It defaults to 'JWT'.
    """
    auth_header_value = request.headers.get('Authorization', None)
    auth_bearer_prefix = current_app.config.get('JWTAUTH_BEARER_PREFIX', 'JWT')
    if not auth_header_value:
        return
    parts = auth_header_value.split()
    if parts[0].lower() != auth_bearer_prefix.lower():
        abort(400, 'Invalid JWT header: Unsupported authorization type')
    elif len(parts) == 1:
        abort(400, 'Invalid JWT header: Token missing')
    elif len(parts) > 2:
        abort(400, 'Invalid JWT header: Token contains spaces')
    if not parts[0]:
        abort(400, 'Authorization required: Request does not contain an access token')
    return parts[1]


def _user_decode(token):
    """
    Retrieves the authenticated user from the payload.

    Secret is taken from configuration key JWTAUTH_SECRET or SECRET_KEY, in that order.

    To specify where to retrieve user name, use JWTAUTH_USER_FIELD.
    """
    try:
        secret = current_app.config.get('JWTAUTH_SECRET', current_app.config.get('SECRET_KEY'))
        user_field = current_app.config.get('JWTAUTH_USER_FIELD', 'login')
        user = jwt.decode(token, secret)[user_field]
    except jwt.InvalidTokenError as e:
        abort(400, ('Invalid JWT', e))
    except KeyError:
        abort(400, ('Invalid JWT', user_field + ' parameter does not exist'))
    return user


def _get_authorization_callback(auth_func, auth_cls, args):
    """
    This function sets the callback function where effective user authorization is done.

    TODO complete this help when we have decided the options offered.
    """
    if auth_func is not None:
        if not callable(auth_func):
            abort(500, 'JWT Authorization: No valid authorization callback function provided')
        return auth_func
    else:
        method = 'auth_{0}'.format(request.method.lower())
        if auth_cls is not None:
            instance = auth_cls()
        else:
            # If no method/class has been passed, maybe first argument is the instance of the same class
            try:
                instance = args[0]
            except IndexError:
                abort(500, 'JWT Authorization: No valid authorization callback function provided')
        try:
            callback = getattr(instance, method)
            return callback
        except AttributeError:
            abort(500, 'JWT Authorization: No valid authorization callback function provided')


def _check_authorization(user, auth_func, **kwargs):
    """
    It calls the authorization function to retrieve the list of authorized users. Then it appends
    admin users so they are always authorized to use full API. This is defined as a list of users
    in configuration key JWTAUTH_API_ADMINS.
    """
    auth_list = auth_func(**kwargs)
    auth_list.extend(current_app.config.get('JWTAUTH_API_ADMINS', []))
    if user in auth_list:
        return
    abort(403, 'JWT Authorization: User is not authorized to access this endpoint')
