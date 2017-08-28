"""
+Capitulo 9 - 
Flask Login + Flask Admin + Flask Redis + Memcached + PostgreSql
https://aws.amazon.com/pt/elasticache/what-is-redis/
https://pypi.python.org/pypi/Flask-And-Redis/0.7
https://pypi.python.org/pypi/Flask-Cache-Redis-Cluster/0.0.5
https://pypi.python.org/pypi/Flask-PyMemcache/0.0.5
https://pypi.python.org/pypi/Flask-Login/0.4.0
https://pypi.python.org/pypi/Flask-Admin/1.5.0

+tentar ver quais os de exemplos podem nos ajudar para criar um 
blog completo com camada de cache/login/admin:
layout
layout_bootstrap3 - so tem playout n tem login
auth-flask-login - mt bom funcoinana mt bem - completo

+criacao de um blog
-admin
-login
-post de um blog
-comentarios
-criacao de post
-camada de cache com redis
-trocar sqlite por PostgreSql ???
-camada de log:
https://pypi.python.org/pypi/Flask-Json-Syslog/0.1.28
testar esta lib, esta 2 anos desatualizada
"""


import os
from flask import Flask, url_for, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from wtforms import form, fields, validators
import flask_admin as admin

from flask_admin.contrib import sqla
from flask_admin import helpers, expose
from werkzeug.security import generate_password_hash, check_password_hash
from app.config import config
from app.form import init
from app.form import admin_index
from app.model import model_view
from app.model import user

# Create Flask application
app = Flask(__name__)

# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = config.flask_app_config['SECRET_KEY']

# Create in-memory database
app.config['DATABASE_FILE'] = config.flask_app_config['DATABASE_FILE']
app.config['SQLALCHEMY_DATABASE_URI'] = config.flask_app_config['SQLALCHEMY_DATABASE_URI'] + config.flask_app_config['DATABASE_FILE']
app.config['SQLALCHEMY_ECHO'] = config.flask_app_config['SQLALCHEMY_ECHO']
db = SQLAlchemy(app)

# Flask views
@app.route('/')
def index():
    return render_template('index.html')

# Initialize flask-login
init.init_login(app)

# Create admin
admin = admin.Admin(app, 'Example: Auth', index_view=admin_index.MyAdminIndexView(), base_template='app/my_master.html')

# Add view
admin.add_view(model_view.MyModelView(user.User, db.session))


if __name__ == '__main__':

    # Build a sample db on the fly, if one does not exist yet.
    app_dir = os.path.realpath(os.path.dirname(__file__))
    database_path = os.path.join(app_dir, app.config['DATABASE_FILE'])
    if not os.path.exists(database_path):
        build_sample_db()

    # Start app
    app.run(debug=True)



