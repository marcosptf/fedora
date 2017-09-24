# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from model import obtem_db as pg
from model import usuario

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
    usuario_id = Column('usuario_id', Integer, ForeignKey('usuario.id'))
    usuarios = relationship("Usuario")
    schema='public'

    def __repr__(self):
        return """
        <Posts(titulo_post='%s', texto_post='%s', data_post='%s', permalink_post='%s', usuario_id='%s')>  
        """ % (self.id, self.titulo_post, self.texto_post, self.data_post, self.permalink_post, self.usuario_id ) 

