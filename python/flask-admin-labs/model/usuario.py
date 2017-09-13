# -*- coding: utf-8 -*-
#criando uma instancia do create_engine
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
        <Usuario(nome='%s', login='%s', email='%s', senha='%s')>
        """ % (self.nome, self.login, self.email, self.senha)
        return """
        <Usuario(id='%s', nome='%s', login='%s', email='%s', senha='%s')>
        """ % (self.id, self.nome, self.login, self.email, self.senha)


