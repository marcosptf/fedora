
from wtforms import form, fields, validators
from sqlalchemy.orm import sessionmaker
from model import obtem_db as pg
from model import usuario

class RegistrationForm(form.Form):
    login = fields.StringField(validators=[validators.required()])
    email = fields.StringField()
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        Session = sessionmaker(bind=pg.obtem_engine())
        session = Session()

        if session.query(usuario.Usuario).filter_by(login=self.login.data).count() > 0:
            raise validators.ValidationError('usuario duplicado')

