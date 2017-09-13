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

usuario = Table('usuario', metadata, 
    Column('id', Integer, primary_key=True),
    Column('nome', String),
    Column('login', String),
    Column('email', String),
    Column('senha', String),
    schema='public'
)

usuarios = [
    { "nome":"java",  "login":"java", "email":"java@java.com", "senha":"123456"  },
    { "nome":"java1", "login":"java1", "email":"java@java.com", "senha":"123456"  },
    { "nome":"java2", "login":"java2", "email":"java@java.com", "senha":"123456"  },
    { "nome":"java3", "login":"java3", "email":"java@java.com", "senha":"123456"  },
    { "nome":"java4", "login":"java4", "email":"java@java.com", "senha":"123456"  }        
]

def createDB():
    metadata.create_all(engine)
    conn = engine.connect()
    conn.execute(usuario.insert(), usuarios)
    
def dropDB():
    metadata.drop_all(engine)
    session.commit()


