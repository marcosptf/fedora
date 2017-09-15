
from wtforms import form, fields, validators
from werkzeug.security import generate_password_hash, check_password_hash

class LoginForm(form.Form):
  
    login = fields.StringField(validators=[validators.required()])
    senha = fields.PasswordField(validators=[validators.required()])

    def obtem_login(self):
        return db.session.query(Usuario).filter_by(login=self.login.data).first()

    def validate_login(self, field):
        usuario = self.obtem_login()

        if usuario is None:
            raise validators.ValidationError('usuario invalido')

        if not check_password_hash(usuario.senha, self.senha.data):
            raise validators.ValidationError('senha incorreta')






