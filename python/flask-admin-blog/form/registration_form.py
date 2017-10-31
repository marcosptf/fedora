
from wtforms import form, fields, validators
from sqlalchemy.orm import sessionmaker
from model import obtem_db as pg
#from model import usuario
from model import tables

class RegistrationForm(form.Form):
  
    nome  = fields.StringField(validators=[validators.required()])
    login = fields.StringField(validators=[validators.required()])
    email = fields.StringField(validators=[validators.required()])
    senha = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        Session = sessionmaker(bind=pg.obtem_engine())
        sessionmk = Session()

        if sessionmk.query(tables.Usuario).filter_by(login=self.login.data).count() > 0:
            raise validators.ValidationError('usuario duplicado')

