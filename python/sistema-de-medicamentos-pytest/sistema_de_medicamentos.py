# -*- coding: utf-8 -*-
"""
sistema de medicamentos
"""

import os, sys
import pymysql.cursors
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

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
    medicamentos = listar_medicamentos()
    return render_template('exibe_painel.html',
                           medicamentos=medicamentos)

def listar_medicamentos():

    medicamentos_json = {
        "medicamento": [{
            "nome": "doril",
            "preco": 3.50,
            "quantidade-comprimidos": 20,
            "desconto-aposentados": "True",
            "desconto-gestantes": "True",
            "farmacia-popular": "True",
            "generico": "False",
            "miligramas": "400mg"
        },{
            "nome": "resfenol",
            "preco": 4.00,
            "quantidade-comprimidos": 10,
            "desconto-aposentados": "True",
            "desconto-gestantes": "True",
            "farmacia-popular": "False",
            "generico": "True",
            "miligramas": "100mg"
        },{
            "nome": "benegrip",
            "preco": 7.50,
            "quantidade-comprimidos": 30,
            "desconto-aposentados": "True",
            "desconto-gestantes": "True",
            "farmacia-popular": "False",
            "generico": "False",
            "miligramas": "20mg"
        },{
            "nome": "buscopan",
            "preco": 5.50,
            "quantidade-comprimidos": 20,
            "desconto-aposentados": "True",
            "desconto-gestantes": "True",
            "farmacia-popular": "True",
            "generico": "False",
            "miligramas": "40mg"
        },{
            "nome": "paracetamol",
            "preco": 4.50,
            "quantidade-comprimidos": 20,
            "desconto-aposentados": "True",
            "desconto-gestantes": "True",
            "farmacia-popular": "True",
            "generico": "True",
            "miligramas": "40mg"
        },{
            "nome": "neosaldina",
            "preco": 3.00,
            "quantidade-comprimidos": 10,
            "desconto-aposentados": "False",
            "desconto-gestantes": "False",
            "farmacia-popular": "False",
            "generico": "False",
            "miligramas": "200mg"
        },{
            "nome": "multigrip",
            "preco": 6.50,
            "quantidade-comprimidos": 20,
            "desconto-aposentados": "True",
            "desconto-gestantes": "False",
            "farmacia-popular": "False",
            "generico": "True",
            "miligramas": "40mg"
        }]
    }
    return medicamentos_json

if __name__ == '__main__'  :
    app.run()

