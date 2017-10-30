# -*- coding: utf-8 -*-

"""
https://pypi.python.org/pypi/Flask-PyMemcache/0.0.5
https://github.com/KLab/Flask-PyMemcache
https://github.com/KLab/Flask-PyMemcache/blob/master/flask_pymemcache.py
"""

from flask import Flask
#from flask_pymemcache import FlaskPyMemcache
import pymemcache.client
import flask_pymemcache

pymc = pymemcache.client.Client(('localhost', 11211))
#memcache = flask.ext.pymemcache.FlaskPyMemcache()
memcache = flask_pymemcache.FlaskPyMemcache()
app = Flask(__name__)
app.config['PYMEMCACHE'] = {
    'server': ('localhost', 11211),
    'key_prefix': b'px',
    'close_on_teardown': False
}

#memcache.init_app(app)
#memcache.client.set(b'foo', b'ola mundo')
#mem_str = memcache.client.get(b'foo')

#PYMEMCACHE = {
    #'server': ('localhost', 11211),
    #'connect_timeout': 1.0,
    #'timeout': 0.5,
    #'no_delay': True,
    #'key_prefix': b'myapp-',
#}

#app.config(dict(
    #DEBUG=True,
    #SECRET_KEY='development key',
    #USERNAME='admin',
    #PASSWORD='default',
    ##conf_key='MEMCACHE_CACHE'
    #conf_key=PYMEMCACHE
#))

#memcache = FlaskPyMemcache()
#memcache.init_app(app, PYMEMCACHE)

#cache = FlaskPyMemcache(conf_key='MEMCACHE_CACHE')
#cache.init_app(app)

@app.route('/')
def ola_mundo():
    memcache.init_app(app)
    memcache.client.set(b'foo', b'ola memcached!')
    return 'aplicacao flask python, %s!' % memcache.client.get(b'foo')

if __name__ == '__main__'  :
    app.run()

