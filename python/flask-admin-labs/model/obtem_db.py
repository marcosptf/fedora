# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, Integer, String

def obtem_url(user='postgres', password='', db='postgres', host='localhost', port=5432, url='postgresql://{}:{}@{}:{}/{}'):
    return url.format(user, password, host, port, db)

def obtem_engine():
    url = obtem_url()
    return sqlalchemy.create_engine(url, client_encoding='utf8')
	
def obtem_metadata():
    engine = obtem_engine()
    return sqlalchemy.MetaData(bind=engine, reflect=True)

