
#postgresql+psycopg2://user:password@host:port/dbname[?key=value&key=value...]

flask_app_config = {
  'SECRET_KEY' : '123456790',
  'SQLALCHEMY_DATABASE_URI' : 'postgresql://postgres:@localhost:5432/postgres',
  'SQLALCHEMY_ECHO' : True
}

