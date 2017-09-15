
from wtforms import form, fields, validators

class RegistrationForm(form.Form):
    login = fields.StringField(validators=[validators.required()])
    email = fields.StringField()
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        if db.session.query(Usuario).filter_by(login=self.login.data).count() > 0:
            raise validators.ValidationError('usuario duplicado')

