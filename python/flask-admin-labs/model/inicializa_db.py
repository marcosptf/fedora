# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, Integer, String, Text, TIMESTAMP, ForeignKey
from model import obtem_db as pg
from DateTime import DateTime

metadata = pg.obtem_metadata()
engine = pg.obtem_engine()

usuarios_dados = [
    { "nome":"admin usuario",  "login":"admin", "email":"admin@java.com", "senha":"pbkdf2:sha256:50000$lndESREy$b44b387c8c1ccdf2a501effccd58843eb24c84fec9e18b3c000c21ee446414ac"  },
    { "nome":"java",  "login":"java", "email":"java@java.com", "senha":"pbkdf2:sha256:50000$lndESREy$b44b387c8c1ccdf2a501effccd58843eb24c84fec9e18b3c000c21ee446414ac"  },
    { "nome":"java1", "login":"java1", "email":"java@java.com", "senha":"pbkdf2:sha256:50000$lndESREy$b44b387c8c1ccdf2a501effccd58843eb24c84fec9e18b3c000c21ee446414ac"  },
    { "nome":"java2", "login":"java2", "email":"java@java.com", "senha":"pbkdf2:sha256:50000$lndESREy$b44b387c8c1ccdf2a501effccd58843eb24c84fec9e18b3c000c21ee446414ac"  },
    { "nome":"java3", "login":"java3", "email":"java@java.com", "senha":"pbkdf2:sha256:50000$lndESREy$b44b387c8c1ccdf2a501effccd58843eb24c84fec9e18b3c000c21ee446414ac"  },
    { "nome":"java4", "login":"java4", "email":"java@java.com", "senha":"pbkdf2:sha256:50000$lndESREy$b44b387c8c1ccdf2a501effccd58843eb24c84fec9e18b3c000c21ee446414ac"  },
]

usuario_tabela = Table('usuario', metadata, 
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('nome', String(50)),
    Column('login', String(25)),
    Column('email', String(50)),
    Column('senha', String(100)),
    schema='public'
)

posts_tabela = Table('posts', metadata, 
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('titulo_post', String(25)),
    Column('texto_post', Text),
    Column('data_post', TIMESTAMP(timezone=True)),
    Column('permalink_post', String(25)),
#    Column('usuario_id', Integer, ForeignKey('usuario.id')),
    Column('usuario_id', Integer),
    schema='public'
)

comentarios_tabela = Table('comentarios', metadata, 
    Column('id', Integer, primary_key=True, autoincrement=True),
#    Column('permalink_post_id', Integer, ForeignKey('posts.id')),
    Column('permalink_post_id', Integer),
    Column('texto_comentario_post', Text),
    Column('data_comentario_post', TIMESTAMP(timezone=True)),
    schema='public'
)

#http://docs.sqlalchemy.org/en/latest/core/metadata.html#sqlalchemy.schema.MetaData.drop_all
tables = [usuario_tabela, posts_tabela, comentarios_tabela]
checkfirst = True

#http://docs.sqlalchemy.org/en/latest/core/metadata.html
#http://docs.sqlalchemy.org/en/latest/orm/tutorial.html
def cria_db():
    metadata.create_all(engine, tables, checkfirst)
    #for i in tables:
    #    i.create(engine)
    #usuario_tabela.create(engine)
    #posts_tabela.create(engine)
    #comentarios_tabela.create(engine)

    conn = engine.connect()
    conn.execute(usuario_tabela.insert(), usuarios_dados)
    
def deleta_db():
    metadata.drop_all(engine, tables, checkfirst)


