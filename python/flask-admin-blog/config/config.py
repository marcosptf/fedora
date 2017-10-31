flask_app_config = {
  'SECRET_KEY' : '123456790',
  'SQLALCHEMY_DATABASE_URI' : 'postgresql://postgres:@localhost:5432/postgres',
  'SQLALCHEMY_ECHO' : True,
  'PYMEMCACHE_HOST' : 'localhost',
  'PYMEMCACHE_PORT' : 11211,
  'PYMEMCACHE_CLOSE' : False,
  'PYMEMCACHE_TIMEOUT_CONN' : 1.0,
  'PYMEMCACHE_TIMEOUT' : 0.5,
  'PYMEMCACHE_NO_DELAY' : True,
  'PYMEMCACHE_KEY_PREFIX' : b'px',
}
