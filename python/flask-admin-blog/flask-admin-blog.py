
import os
from flask import Flask, url_for, redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from wtforms import form, fields, validators
from werkzeug.security import generate_password_hash, check_password_hash
from config import config
from form import init, admin_index
from model import tables
from flask_script import Manager
from model import obtem_db as pg
from sqlalchemy.orm import sessionmaker
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = config.flask_app_config['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = config.flask_app_config['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_ECHO'] = config.flask_app_config['SQLALCHEMY_ECHO']
db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def index():
    Session = sessionmaker(bind=pg.obtem_engine())
    sessionmk = Session()
    init_flask_login()
    pq = sessionmk.query(tables.Posts.titulo_post, tables.Posts.data_post, tables.Posts.permalink_post, tables.Usuario.login).join(tables.Usuario).filter(tables.Usuario.id == tables.Posts.usuario_id).all()
    return render_template('index.html', posts_links=pq)

@app.route('/salva_comentario_post', methods=['POST'])
def salva_comentario_post():
    data_form = request.form 
    salva_comentario(data_form)
    return redirect(url_for('.exibe_posts', post_permalink=data_form['permalink_post']))

def salva_comentario(dados_post):
    Session = sessionmaker(bind=pg.obtem_engine())
    sessionmk = Session()
    novo_comentario = tables.Comentarios(permalink_comentario_post=dados_post['permalink_post'], texto_comentario_post=dados_post['comentario'], data_comentario_post=datetime.now(), post_id=dados_post['post_id'])
    sessionmk.add(novo_comentario)
    sessionmk.commit()

@app.route('/exibe_posts/<string:post_permalink>', methods=['GET'])
def exibe_posts(post_permalink):
    Session = sessionmaker(bind=pg.obtem_engine())
    sessionmk = Session()
    init_flask_login()
    posts_links = sessionmk.query(tables.Posts.id, tables.Posts.texto_post, tables.Posts.titulo_post, tables.Posts.data_post, tables.Posts.permalink_post, tables.Usuario.login).filter(tables.Posts.permalink_post==post_permalink).filter(tables.Posts.usuario_id==tables.Usuario.id).first()
    posts_comentarios = sessionmk.query(tables.Comentarios.texto_comentario_post,tables.Comentarios.data_comentario_post).filter(tables.Comentarios.post_id==posts_links.id).all()    
    return render_template('exibe_posts.html', post=posts_links, posts_comentarios=posts_comentarios)

@app.template_filter('strftime')
def _jinja2_filter_datetime(date):
    from dateutil.parser import parse
    date = parse(date)
    format='%d/%m/%Y %X'
    return date.strftime(format)

def init_flask_login():
    import flask_admin as fadmin
    from flask_admin.contrib.sqla import ModelView
    
    init.init_login(app)
    cadmin = fadmin.Admin(app, 'Blog Admin', index_view=admin_index.MyAdminIndexView(), base_template='my_master.html')
    #aqui nos podemos usar a view do posts criada pelo flask-admin;
    #deixamos comentada porque vamos usar a nossa propria customizada para criar posts
    #cadmin.add_view(ModelView(tables.Posts, db.session))
    cadmin.add_view(ModelView(tables.Usuario, db.session))
    cadmin.add_view(ModelView(tables.Comentarios, db.session))

manager = Manager(app)

@manager.command
def cria_db():
    tables.cria_db()
    
@manager.command
def deleta_db():
    tables.deleta_db()
    
if __name__ == '__main__':
    manager.run()


