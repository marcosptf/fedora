
from wtforms import form, fields, validators
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import sessionmaker
from model import obtem_db as pg
from model import tables

class LoginForm(form.Form):

    login = fields.StringField(validators=[validators.required()])
    senha = fields.PasswordField(validators=[validators.required()])

    def obtem_login(self):
        Session = sessionmaker(bind=pg.obtem_engine())
        sessionmk = Session()
        return sessionmk.query(tables.Usuario).filter_by(login=self.login.data).first()

    def validate_login(self, field):
        usuario = self.obtem_login()

        if usuario is None:
            raise validators.ValidationError('usuario invalido')

        if not check_password_hash(usuario.senha, self.senha.data):
            raise validators.ValidationError('senha incorreta')

