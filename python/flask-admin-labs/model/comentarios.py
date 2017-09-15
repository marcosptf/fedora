# -*- coding: utf-8 -*-
#criando uma instancia do create_engine
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

class Comentarios(Base):
    __tablename__ = 'comentarios'

    id = Column(Integer, primary_key=True)
    permalink_comentario_post = Column(String(250))
    texto_comentario_post = Column(String(250))
    data_comentario_post = Column(String(250))
    schema='public'

    def __repr__(self):
        return """
        <Comentarios(id='%s', permalink_comentario_post='%s', texto_comentario_post='%s', data_comentario_post='%s')>
        """ % (self.id, self.permalink_comentario_post, self.texto_comentario_post, self.data_comentario_post)

