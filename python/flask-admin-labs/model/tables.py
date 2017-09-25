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
    schema='public'

    def __repr__(self):
        return """
        <Comentarios(id='%s', permalink_comentario_post='%s', texto_comentario_post='%s', data_comentario_post='%s')>
        """ % (self.id, self.permalink_comentario_post, self.texto_comentario_post, self.data_comentario_post)

class Posts(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    titulo_post = Column(String(250))
    texto_post = Column(String(250))
    data_post = Column(String(250))
    permalink_post = Column(String(250))
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    #posts_rel = relationship("Usuario", back_populates="usuario_rel")
    posts_rel = relationship("Usuario", foreign_keys="[Posts.usuario_id]")
    schema='public'

    def __repr__(self):
        return """
        <Posts(titulo_post='%s', texto_post='%s', data_post='%s', permalink_post='%s', usuario_id='%s', posts_rel='%s')>  
        """ % (self.id, self.titulo_post, self.texto_post, self.data_post, self.permalink_post, self.usuario_id, self.posts_rel) 

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True)
    nome = Column(String(250))
    login = Column(String(250))
    email = Column(String(250))
    senha = Column(String(250))
    usuario_rel = relationship("Posts", foreign_keys=["Usuario.id"])
    #posts_rel = relationship("Usuario", foreign_keys="[Posts.usuario_id]")
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
        <Usuario(nome='%s', login='%s', email='%s', senha='%s', usuario_rel='%s')>
        """ % (self.id, self.nome, self.login, self.email, self.senha, self.usuario_rel)

# Create customized model view class
class MyModelView(sqla.ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated

    def obtem_usuario(self):
        return login



