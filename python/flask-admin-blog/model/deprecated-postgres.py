# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, Integer, String

user='postgres'
password=''
db='postgres'
host='localhost'
port=5432
url = 'postgresql://{}:{}@{}:{}/{}'

url = url.format(user, password, host, port, db)
engine = sqlalchemy.create_engine(url, client_encoding='utf8')
metadata = sqlalchemy.MetaData(bind=engine, reflect=True)
#engine = create_engine("mysql://root:123456@localhost:3306/sistema_de_contatos", echo=True)
Base = declarative_base()
'''
criando uma instancia de session
'''
Session = sessionmaker(bind=engine)
session = Session()

