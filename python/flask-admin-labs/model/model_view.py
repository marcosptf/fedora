
import flask_login as login
from flask_admin.contrib import sqla

# Create customized model view class
class MyModelView(sqla.ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated

    def obtem_usuario(self):
        return login
