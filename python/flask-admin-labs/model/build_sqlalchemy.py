# -*- coding: utf-8 -*-
#criando uma instancia do create_engine
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
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

'''
criando uma instancia de session
'''
Session = sessionmaker(bind=engine)
session = Session()

#vamos retirar daqui esta classe e criar uma entidade num outro arquivo e deixar este aki somente para
#para criar/deletar base via linha de comando

"""
class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True),
    nome = Column('nome', String),
    login = Column('login', String),
    email = Column('email', String),
    senha = Column('senha', String)
    schema='public'

#    def __repr__(self):
#        return """
#        <Usuario(nome='%s', login='%s', email='%s', senha='%s')>
#        """ % (self.nome, self.login, self.email, self.senha)
#        return """
#        <Usuario(id='%s', nome='%s', login='%s', email='%s', senha='%s')>
#        """ % (self.id, self.nome, self.login, self.email, self.senha)

usuario = Table('usuario', metadata, 
    Column('id', Integer, primary_key=True),
    Column('nome', String),
    Column('login', String),
    Column('email', String),
    Column('senha', String),
    schema='public'
)

usuarios = [
    { "nome":"java",  "login":"java", "email":"java@java.com", "senha":"123456"  },
    { "nome":"java1", "login":"java1", "email":"java@java.com", "senha":"123456"  },
    { "nome":"java2", "login":"java2", "email":"java@java.com", "senha":"123456"  },
    { "nome":"java3", "login":"java3", "email":"java@java.com", "senha":"123456"  },
    { "nome":"java4", "login":"java4", "email":"java@java.com", "senha":"123456"  }        
]

#funciona muito bem sem warnings
def createDB():
    #Base.metadata.create_all(engine)
    metadata.create_all(engine)
    session.commit()    
    conn = engine.connect()
    conn.execute(usuario.insert(), usuarios)
    #engine.execute(metadata.tables['usuario'].insert, usuarios)    

#funciona bem mais esta gerando warnings    
#debuga depois isto
#possivel solucao seria agente fazer uma validacao para ver se existe algo a ser deletado antes
def dropDB():
    #Base.metadata.drop_all(engine)
    metadata.drop_all(engine)
    session.commit()


