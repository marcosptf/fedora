# -*- coding: utf-8 -*-
"""
sistema de medicamentos
"""

import os, sys
import pymysql.cursors
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from lista_medicamentos_json import medicamento

'''
Aqui é criado a aplicacao flask
'''
app = Flask(__name__)

'''
Aqui é adicionado as configuracoes da aplicacao
'''
app.config.update(dict( DEBUG="True", SECRET_KEY='sistema-de-medicamentos-key' ))

@app.route('/')
def index():
    med = medicamento()
    medicamentos = med.lista_medicamentos_json()
    return render_template('exibe_painel.html',
			   medicamentos=medicamentos)

if __name__ == '__main__'  :
    app.run()

