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

class Comentarios(Base):
    __tablename__ = 'comentarios'

    id = Column(Integer, primary_key=True),
    permalink_comentario_post = Column('permalink_comentario_post', String)
    texto_comentario_post = Column('texto_comentario_post', String),
    data_comentario_post = Column('data_comentario_post', String),
    schema='public'

    def __repr__(self):
        return """
        <Comentarios(id='%s', permalink_comentario_post='%s', texto_comentario_post='%s', data_comentario_post='%s')>
        """ % (self.id, self.permalink_comentario_post, self.texto_comentario_post, self.data_comentario_post)

