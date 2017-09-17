
import flask_admin as admin 
from flask_admin import helpers, expose
import flask_login as login
from flask import Flask, url_for, redirect, render_template, request
from login_form import LoginForm
from cria_post_form import CriaPostForm
from registration_form import RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import sessionmaker
from model import obtem_db as pg
from model.posts import Posts
from model.usuario import Usuario

# Create customized index view class that handles login & registration
class MyAdminIndexView(admin.AdminIndexView):

    @expose('/')
    def index(self):
        print("route-root-admin");
        if not login.current_user.is_authenticated:
            return redirect(url_for('.login_view'))
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
        link = '<p>nao tem conta ainda ?<a href="' + url_for('.register_view') + '">crie uma conta agora!</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()
      
    @expose('/criapost/', methods=('GET', 'POST'))
    def criapost(self):
        print("route-criapost-admin");
        #form = CriaPostForm(request.form)
        #form.obtem_cria_post()
        data_form = request.form
        #data_form['texto_post']
        #data_form['titulo_post']
        Session = sessionmaker(bind=pg.obtem_engine())
        session = Session()
        posts = Posts()
        posts.titulo_post = data_form['titulo_post']
        posts.texto_post = data_form['texto_post']
        #pendencias
        #criar timestamp para o data post
        #crir vinculo de post x usuario
        data_post = None 
        permalink_post = None
        session.add(posts)
        session.commit()
        return super(MyAdminIndexView, self).index()

    @expose('/register/', methods=('GET', 'POST'))
    def register_view(self):
        print("route-register-admin");
        form = RegistrationForm(request.form)
        
        if helpers.validate_form_on_submit(form):
            Session = sessionmaker(bind=pg.obtem_engine())
            session = Session()
            usuario = Usuario()
            form.populate_obj(usuario)
            usuario.senha = generate_password_hash(form.password.data)
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

