"""
+Capitulo 9 - 
Flask Login + Flask Admin + Flask Redis + Memcached + PostgreSql
https://aws.amazon.com/pt/elasticache/what-is-redis/
https://pypi.python.org/pypi/Flask-And-Redis/0.7
https://pypi.python.org/pypi/Flask-Cache-Redis-Cluster/0.0.5
https://pypi.python.org/pypi/Flask-PyMemcache/0.0.5
https://pypi.python.org/pypi/Flask-Login/0.4.0
https://pypi.python.org/pypi/Flask-Admin/1.5.0
https://docs.python.org/2/tutorial/datastructures.html
http://docs.sqlalchemy.org/en/latest/orm/tutorial.html
https://flask-script.readthedocs.io/en/latest/
https://suhas.org/sqlalchemy-tutorial/
http://docs.sqlalchemy.org/en/latest/core/metadata.html#sqlalchemy.schema.Table
https://www.elephantsql.com/?gclid=EAIaIQobChMIy9fUqaeT1gIVnLrACh2jpwQ_EAAYASAAEgJ8TvD_BwE
https://www.postgresql.org/docs/9.6/static/sql-expressions.html
http://docs.sqlalchemy.org/en/latest/dialects/postgresql.html#module-sqlalchemy.dialects.postgresql.psycopg2
https://pypi.python.org/pypi?%3Aaction=search&term=psycopg2&submit=search
http://flask-admin.readthedocs.io/en/latest/advanced/

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

+tutorial sqlalchemy + postgresql
https://suhas.org/sqlalchemy-tutorial/

#dependencia para instalar psycopg2
dnf install libpqxx-devel libpqxx

#deletar todos os arquivos .pyc
find . -name '*.pyc' -print | xargs /bin/rm -rfv

#refatoracao
1.refatorar a model para funcionar o sqlalchemy orm para persistencias
colocar estes arquivos como deprecated:
build.py
build_sqlalchemy.py
postgres.py
user.py
2.testar para ver se o flask-admin funciona corretamento com o postgresql
3.criar uma tela inicial simples para o blog
==>>>4.criar uma nova tela no admin para criar posts
5.na tela do blog, exibir os posts
6.no front, cada titulo do blog deve ser um permalink para uma pagina daquele post
7.na pagina deste post deve mostrar o post completo + opcao para comentarios publicos
8.depois vamos aplicar o memcached para a camada front no blog
9.criar logs usando:
https://docs.python.org/2/howto/logging.html
http://flask.pocoo.org/docs/0.12/errorhandling/#error-logging-tools

#exemplo de query sqlalchemy usando session
#mais exemplos:
#http://docs.sqlalchemy.org/en/latest/orm/tutorial.html
from sqlalchemy.orm import sessionmaker
from model import obtem_db as pg

Session = sessionmaker(bind=pg.obtem_engine())
session = Session()

contato = session.query(Contatos).filter_by(id=id).first()
session.delete(contato)
session.commit()

#implementar logs
https://logbook.readthedocs.io/en/stable/
https://pypi.python.org/pypi/logzero

"""

import os
from flask import Flask, url_for, redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from wtforms import form, fields, validators
#from flask_admin.contrib import sqla
from flask_admin import helpers, expose
from werkzeug.security import generate_password_hash, check_password_hash
from config import config
from form import init, admin_index
#from model import model_view, posts, usuario, comentarios, inicializa_db_labs
from model import tables
from flask_script import Manager
from model import obtem_db as pg
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.config['SECRET_KEY'] = config.flask_app_config['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = config.flask_app_config['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_ECHO'] = config.flask_app_config['SQLALCHEMY_ECHO']
db = SQLAlchemy(app)

@app.route('/')
def index():
    Session = sessionmaker(bind=pg.obtem_engine())
    sessionmk = Session()
    init_flask_login()
    #posts_links = sessionmk.query(posts.Posts).filter_by(id=1).first()
    #posts_query = sessionmk.query(posts.Posts, usuario.Usuario).filter(usuario.Usuario.id == posts.Posts.usuario_id).all()
    pq = sessionmk.query(tables.Posts).join(tables.Usuario).filter(tables.Usuario.id == tables.Posts.usuario_id).all()
#    pq = posts_query.all()
#    for q in pq:
#        print("debugger-query=>")
#        print(q['titulo_post'])
    return render_template('index.html', posts_links=pq)

#@app.route('/exibe_posts/<string:post_permalink>')
#def exibe_posts(post_permalink):
#    Session = sessionmaker(bind=pg.obtem_engine())
#    sessionmk = Session()
#    init_flask_login()
#    posts_links = sessionmk.query(tables.Posts).filter_by(permalink_post=post_permalink).first()
#    return render_template('index.html', posts_links=posts_links)


def init_flask_login():
    import flask_admin as fadmin
    
    #example app.py
    #admin.add_view(MyModelView(User, db.session))
    init.init_login(app)
    
    #o erro que esta dando naotem absolutamente nada a ver
    #com os parametros da instancia abaixo ===>>>
    cadmin = fadmin.Admin(app, 'Blog Admin', index_view=admin_index.MyAdminIndexView(), base_template='my_master.html')
    #cadmin = fadmin.Admin(app)
    
    #tentar fazer conforme este exemplo:
    #exemplo mais basico possivel ===>>>
    #1.https://flask-admin.readthedocs.io/en/v1.0.7/db_sqla/
    #2.https://stackoverflow.com/questions/33698104/flask-admin-editing-relationship-giving-me-object-representation-of-foreign-key
    #3.http://flask-admin.readthedocs.io/en/latest/api/mod_contrib_sqla/
    
    
    #quando descomenta estas linhas error SQLAlchemy
    #from flask.ext.admin.contrib.sqla import ModelView
    from flask_admin.contrib.sqla import ModelView
    cadmin.add_view(ModelView(tables.Posts, db.session))
    cadmin.add_view(ModelView(tables.Usuario, db.session))
    
    #admin.add_view(model_view.MyModelView(posts.Posts, db.session))
    #admin.add_view(model_view.MyModelView(usuario.Usuario, db.session))
    #admin.add_view(model_view.MyModelView(comentarios.Comentarios, db.session))

manager = Manager(app)

#python flask-admin-labs.py gera_db
@manager.command
def cria_db():
    tables.cria_db()
    
#python flask-admin-labs.py deleta_db
@manager.command
def deleta_db():
    tables.deleta_db()
    
if __name__ == '__main__':
    manager.run()



