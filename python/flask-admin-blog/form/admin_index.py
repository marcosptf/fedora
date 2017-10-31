
import flask_admin as fadmin 
from flask_admin import helpers, expose
import flask_login as login
from flask import Flask, url_for, redirect, render_template, request, session
from login_form import LoginForm
from cria_post_form import CriaPostForm
from registration_form import RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import sessionmaker
from model import obtem_db as pg
from datetime import datetime
from model import tables

class MyAdminIndexView(fadmin.AdminIndexView):

    @expose('/')
    def index(self):

        if not login.current_user.is_authenticated:
            return redirect(url_for('.login_view'))
	
        Session = sessionmaker(bind=pg.obtem_engine())
        sessionmk = Session()	
        qtde_usuarios = sessionmk.query(tables.Usuario).count()
        qtde_posts = sessionmk.query(tables.Posts).count()
        qtde_comentarios = sessionmk.query(tables.Comentarios).count()
        self._template_args['qtde_usuarios'] = qtde_usuarios
        self._template_args['qtde_posts'] = qtde_posts
        self._template_args['qtde_comentarios'] = qtde_comentarios
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        print("route-login-admin");
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.obtem_login()
            login.login_user(user)

        if login.current_user.is_authenticated:
            return redirect(url_for('.index'))
        link = '<p>nao tem conta ainda ?<a href="' + url_for('.register_view') + '"> crie uma conta agora!</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/register/', methods=('GET', 'POST'))
    def register_view(self):
        print("route-register-admin");
        form = RegistrationForm(request.form)
        
        if helpers.validate_form_on_submit(form):
            Session = sessionmaker(bind=pg.obtem_engine())
            session = Session()
            usuario = tables.Usuario()
            form.populate_obj(usuario)
            usuario.senha = generate_password_hash(form.senha.data)
            session.add(usuario)
            session.commit()
            login.login_user(usuario)
            return redirect(url_for('.index'))

        link = '<p>ja tem uma conta? <a href="' + url_for('.login_view') + '">acesse</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))
