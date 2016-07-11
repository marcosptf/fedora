# -*- coding: utf-8 -*-
"""
    sistema de pontos

    Esta aplicacao exemplo Flask, eh um simulador de sistema de espera.
    Flask and sqlite3.
"""

from flask import Flask

app = Flask(__name__)

def funcao_um():
    return "funcao um "

def funcao_dois():
    return 'funcao dois'

@app.route('/')
def index():
    import ipdb; ipdb.set_trace();
    func_um = funcao_um()
    func_dois = funcao_dois()
    resp = func_um + func_dois
    #import ipdb; ipdb.set_trace();
    return resp

if __name__ == '__main__'  :
    app.run()

