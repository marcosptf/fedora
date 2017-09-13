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

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True),
    nome = Column('nome', String),
    login = Column('login', String),
    email = Column('email', String),
    senha = Column('senha', String)
    schema='public'

    def __repr__(self):
        return """
        <Usuario(id='%s', nome='%s', login='%s', email='%s', senha='%s')>
        """ % (self.id, self.nome, self.login, self.email, self.senha)

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    # Required for administrative interface
    def __unicode__(self):
        return self.nome

