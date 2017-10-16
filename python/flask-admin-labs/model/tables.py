# -*- coding: utf-8 -*-

#criando uma instancia do create_engine
import sqlalchemy
from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from model import obtem_db as pg
import flask_login as login
from flask_admin.contrib import sqla

metadata = pg.obtem_metadata()
engine = pg.obtem_engine()
Base = declarative_base()

class Comentarios(Base):
    __tablename__ = 'comentarios'

    id = Column(Integer, primary_key=True)
    permalink_comentario_post = Column(String(250))
    texto_comentario_post = Column(String(250))
    data_comentario_post = Column(String(250))
    post_id = Column(Integer)
    #post_id = Column(Integer, ForeignKey('posts.id'))
    schema='public'

    def __repr__(self):
        return """
        <Comentarios(id='%s', permalink_comentario_post='%s', texto_comentario_post='%s', data_comentario_post='%s', post_id='%s')>
        """ % (self.id, self.permalink_comentario_post, self.texto_comentario_post, self.data_comentario_post, self.post_id)

class Posts(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    titulo_post = Column(String(250))
    texto_post = Column(String(250))
    data_post = Column(String(250))
    permalink_post = Column(String(250))
    usuario_id = Column(Integer)
    #usuario_id = Column(Integer, ForeignKey('usuario.id'))
    #usuario_rel = relationship("Usuario")
    schema='public'

    def __repr__(self):
        return """
        <Posts(titulo_post='%s', texto_post='%s', data_post='%s', permalink_post='%s', usuario_id='%s')>  
        """ % (self.id, self.titulo_post, self.texto_post, self.data_post, self.permalink_post, self.usuario_id) 

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True)
    nome = Column(String(250))
    login = Column(String(250))
    email = Column(String(250))
    senha = Column(String(250))
    #usuario_rel = relationship("Posts")
    schema='public'

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __unicode__(self):
        return self.nome

    def __repr__(self):
        return """
        <Usuario(nome='%s', login='%s', email='%s', senha='%s')>
        """ % (self.id, self.nome, self.login, self.email, self.senha)

# Create customized model view class
class MyModelView(sqla.ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated

    #def obtem_usuario(self):
        #return login

def cria_db():

    Base.metadata.create_all(engine)

    usuarios_dados = [
        { "nome":"admin usuario",  "login":"admin", "email":"admin@java.com", "senha":"pbkdf2:sha256:50000$lndESREy$b44b387c8c1ccdf2a501effccd58843eb24c84fec9e18b3c000c21ee446414ac"  },
        { "nome":"java",  "login":"java", "email":"java@java.com", "senha":"pbkdf2:sha256:50000$lndESREy$b44b387c8c1ccdf2a501effccd58843eb24c84fec9e18b3c000c21ee446414ac"  },
        { "nome":"java1", "login":"java1", "email":"java@java.com", "senha":"pbkdf2:sha256:50000$lndESREy$b44b387c8c1ccdf2a501effccd58843eb24c84fec9e18b3c000c21ee446414ac"  },
        { "nome":"java2", "login":"java2", "email":"java@java.com", "senha":"pbkdf2:sha256:50000$lndESREy$b44b387c8c1ccdf2a501effccd58843eb24c84fec9e18b3c000c21ee446414ac"  },
        { "nome":"java3", "login":"java3", "email":"java@java.com", "senha":"pbkdf2:sha256:50000$lndESREy$b44b387c8c1ccdf2a501effccd58843eb24c84fec9e18b3c000c21ee446414ac"  },
        { "nome":"java4", "login":"java4", "email":"java@java.com", "senha":"pbkdf2:sha256:50000$lndESREy$b44b387c8c1ccdf2a501effccd58843eb24c84fec9e18b3c000c21ee446414ac"  },
    ]

    #posts = Posts()
    #usuario = Usuario()
    #usuario.nome = usuarios_dados['0']['nome']
    #usuario.login = usuarios_dados['0']['login']
    #usuario.email = usuarios_dados['0']['email']
    #usuario.senha = usuarios_dados['0']['senha']

    #Session = sessionmaker(bind=pg.obtem_engine())
    #sessionmk = Session()
    #sessionmk.add(usuario)
    #sessionmk.commit()

def deleta_db():
    Base.metadata.drop_all(engine)



