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
Base = declarative_base()

class Posts(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    titulo_post = Column(String(250))
    texto_post = Column(String(250))
    data_post = Column(String(250))
    permalink_post = Column(String(250))
    schema='public'

    def __repr__(self):
        return """
        <Posts(titulo_post='%s', texto_post='%s', data_post='%s', permalink_post='%s')>
        """ % (self.id, self.titulo_post, self.texto_post, self.data_post, self.permalink_post)

