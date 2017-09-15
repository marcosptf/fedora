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

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True)
    nome = Column(String(250))
    login = Column(String(250))
    email = Column(String(250))
    senha = Column(String(250))
    schema='public'

    def __repr__(self):
        return """
        <Usuario(nome='%s', login='%s', email='%s', senha='%s')>
        """ % (self.id, self.nome, self.login, self.email, self.senha)



