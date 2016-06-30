# -*- coding: utf-8 -*-
"""
    sistema de pontos

    Esta aplicacao exemplo Flask, eh um simulador de sistema de espera.
    Flask and sqlite3.
"""

'''
Aqui, é onde realizamos todas as importações dos componentes e pacotes 
instalados pelo pip.
O termo "from" significa neste contexo, "a partir deste pacote";
O termo "import" significa, "somente traga";

vamos ver como fica por exemplo a linha x
from sqlalchemy.orm import relationship
A partir do pacote sqlalchemy.orm, me traga o componente relationship;

Isto significa que, o flask, fará uso do componente relationship que está dentro do pacote sqlalchemy.orm;

'''
import os, sys
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

'''
Aqui é criado a aplicacao flask
'''
app = Flask(__name__)


'''
Aqui é adicionado as configuracoes da aplicacao
'''
app.config.update(dict( DEBUG=True ))

@app.route('/')
def index():
    dados = ""  
    return render_template('exibe_painel.html', dados=dados)
  
@app.route('/proxima-senha')  
def proxima_senha():  
    mariadb_ = obtem_mariadb()

    return render_template('exibe_painel.html', dados=dados)


create table painel (
 id integer primary key auto_increment,
 senha_prioridade integer default 0,
 senha_atendida   integer default 0
);

def obtem_mariadb();
pass
  
def gera_proxima_senha():
    resp = sqlite.execute('select id from display where atendido=0 order by senha_prioridade desc limit 1')
    dados = resp.fetchall()

    if hasattr(dados, 'id'):
        sqlite.execute('update display set atendido=1 where id = ?', dados['id']) #tem que testar e ver se eh assim msm :-)
  






if __name__ == '__main__'  :
    app.run()

