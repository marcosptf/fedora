
import sqlalchemy

def connect(user='postgres', password='', db='postgres', host='localhost', port=5432):

    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)
    conn = sqlalchemy.create_engine(url, client_encoding='utf8')
    meta = sqlalchemy.MetaData(bind=conn, reflect=True)

    return con, meta
  
  