
from config import config
from model import obtem_db as pg
from sqlalchemy.orm import sessionmaker
from flask import Flask, url_for, redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from model import tables
from pprint import pprint


app = Flask(__name__)
app.config['SECRET_KEY'] = config.flask_app_config['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = config.flask_app_config['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_ECHO'] = config.flask_app_config['SQLALCHEMY_ECHO']
db = SQLAlchemy(app)

Session = sessionmaker(bind=pg.obtem_engine())
sessionmk = Session()
pq = sessionmk.query(tables.Posts).join(tables.Usuario).filter(tables.Usuario.id == tables.Posts.usuario_id).all()
#pq = sessionmk.query(tables.Usuario).all()
#pq = user_query.all()

print("debugger-for=>")
for q in pq:
    print("debugger-query=>")
    print(q.permalink_post)


#a = tables.Posts();
#pprint(a)
