# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, Integer, String
from model import obtem_db as pg

metadata = pg.obtem_metadata()
engine = pg.obtem_engine()

usuarios_dados = [
    { "nome":"java",  "login":"java", "email":"java@java.com", "senha":"123456"  },
    { "nome":"java1", "login":"java1", "email":"java@java.com", "senha":"123456"  },
    { "nome":"java2", "login":"java2", "email":"java@java.com", "senha":"123456"  },
    { "nome":"java3", "login":"java3", "email":"java@java.com", "senha":"123456"  },
    { "nome":"java4", "login":"java4", "email":"java@java.com", "senha":"123456"  }        
]

usuario_tabela = Table('usuario', metadata, 
    Column('id', Integer, primary_key=True),
    Column('nome', String),
    Column('login', String),
    Column('email', String),
    Column('senha', String),
    schema='public'
)

posts_tabela = Table('posts', metadata, 
    Column('id', Integer, primary_key=True),
    Column('titulo_post', String),
    Column('texto_post', String),
    Column('data_post', String), #mudar para timestamp
    Column('permalink_post', String),
    schema='public'
)	

comentarios_tabela = Table('comentarios', metadata, 
    Column('id', Integer, primary_key=True),
    Column('permalink_comentario_post', String),
    Column('texto_comentario_post', String),
    Column('data_comentario_post', String), #mudar para timestamp
    schema='public'
)	

def cria_db():
    metadata.create_all(engine)
    conn = engine.connect()
    conn.execute(usuario_tabela.insert(), usuarios_dados)
    
def deleta_db():
    metadata.drop_all(engine)


