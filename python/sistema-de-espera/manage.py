# -*- coding: utf-8 -*-
"""
    sistema de pontos

    Esta aplicacao exemplo Flask, eh um simulador de sistema de espera.
    Flask and sqlite3.
"""

import os, click
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
#from flask_script import Manager   

app = Flask(__name__)

@app.route('/')
def ola_mundo():
    return 'aplicacao flask python, ola mundo!'
  
if __name__ == '__main__'  :
    app.run()


