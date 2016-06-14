# -*- coding: utf-8 -*-
"""
    sistema de pontos
    ~~~~~~

    Esta aplicacao exemplo Flask, eh um simulador de sistema de espera.
    Flask and sqlite3.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""

import os
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash


# create our little application :)
app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connecta_sqlite():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def inicializa_sqlite():
    """Initializes the database."""
    sq = obtem_sqlite()
    with app.open_resource('schema.sql', mode='r') as f:
        sq.cursor().executescript(f.read())
    sq.commit()


@app.cli.command('inicializa_sqlite')
def inicializasqite_command():
    """Creates the database tables."""
    inicializa_sqlite()
    print('Initialized the database.')


def obtem_sqlite():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = conecta_sqlite()
    return g.sqlite_db


def fecha_sqlite(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/')
def exibe_painel():
    sqlite = obtem_sqlite()
    resp = sqlite.execute('select title, text from entries order by id desc')
    dados = resp.fetchall()
    return render_template('exibe_painel.html', dados=dados)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    sqlite = obtem_sqlite()
    sqlite.execute('insert into entries (title, text) values (?, ?)',
               [request.form['title'], request.form['text']])
    sqlite.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))
