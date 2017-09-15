
import flask_admin as admin 
from flask_admin import helpers, expose
import flask_login as login
from flask import Flask, url_for, redirect, render_template, request
from login_form import LoginForm
from registration_form import RegistrationForm
from model.usuario import Usuario

# Create customized index view class that handles login & registration
class MyAdminIndexView(admin.AdminIndexView):

    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login.login_user(user)

        if login.current_user.is_authenticated:
            return redirect(url_for('.index'))
        link = '<p>nao tem conta ainda ?<a href="' + url_for('.register_view') + '">crie uma conta agora!</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/register/', methods=('GET', 'POST'))
    def register_view(self):
        form = RegistrationForm(request.form)
        
        if helpers.validate_form_on_submit(form):
            usuario = Usuario()
            form.populate_obj(usuario)
            usuario.senha = generate_password_hash(form.password.data)
            db.session.add(usuario)
            db.session.commit()

            login.login_user(user)
            return redirect(url_for('.index'))
        link = '<p>ja tem uma conta? <a href="' + url_for('.login_view') + '">acesse</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))

