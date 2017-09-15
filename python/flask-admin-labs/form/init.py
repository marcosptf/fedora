
import flask_login as login
from sqlalchemy.orm import sessionmaker
from model import obtem_db as pg
from model import usuario

def init_login(app):
    login_manager = login.LoginManager()
    login_manager.init_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        Session = sessionmaker(bind=pg.obtem_engine())
        session = Session()
        return session.query(usuario.Usuario).get(user_id)

