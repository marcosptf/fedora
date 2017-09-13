# -*- coding: utf-8 -*-
#criando uma instancia do create_engine
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, Integer, String
from model import postgres as pg

metadata = pg.obtem_metadata_postgres()
engine = pg.obtem_engine_postgres()
Base = declarative_base()

class Posts(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True),
    titulo_post = Column('titulo_post', String),
    texto_post = Column('texto_post', String),
    data_post = Column('data_post', String),
    permalink_post = Column('permalink_post', String)
    schema='public'

    def __repr__(self):
        return """
        <Posts(id='%s', titulo_post='%s', texto_post='%s', data_post='%s', permalink_post='%s')>
        """ % (self.id, self.titulo_post, self.texto_post, self.data_post, self.permalink_post)

