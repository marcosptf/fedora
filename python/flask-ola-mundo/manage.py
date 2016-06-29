# -*- coding: utf-8 -*-
"""
    sistema de pontos

    Esta aplicacao exemplo Flask, eh um simulador de sistema de espera.
    Flask and sqlite3.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def ola_mundo():
    return 'aplicacao flask python, ola mundo!'
  
if __name__ == '__main__'  :
    app.run()

