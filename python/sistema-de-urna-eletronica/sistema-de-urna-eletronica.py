# -*- coding: utf-8 -*-
"""
    sistema de pontos

    Esta aplicacao exemplo Flask, eh um simulador de sistema de espera.
    Flask and sqlite3.
    
carioca-panico.jpg
danilo-gentili.jpg
joselito-hermes-e-renato.jpg
rafinha-bastos.jpg
sergio-mallandro.jpg
    
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


#comandos usados para criar database no pymongo
>>> from pymongo import MongoClient
>>> client = MongoClient()
>>> client
MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True)
>>> 
>>> db = client.urna_database
>>> db
Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), u'urna_database')
>>> collection = db.urna_collection
>>> collection
Collection(Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), u'urna_database'), u'urna_collection')
>>> 


'''
import os, sys
from pymongo import MongoClient
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

'''
Aqui é criado a aplicacao flask
'''
app = Flask(__name__)


'''
Aqui é adicionado as configuracoes da aplicacao
'''
app.config.update(dict( DEBUG=True, SECRET_KEY='sistema-de-urna-eletronica-key' ))

eleitor = ""
candidato = ""


@app.route('/')
def index():
    #ultima_senha = ultima_senha_chamada()
    #ver_relatorio = ver_relatorio_paciente()
    return render_template('index_urna.html')
                         
			   #,ver_relatorio = ver_relatorio)

@app.route('/identificacao_do_eleitor', methods=['GET'])
def identificacao_do_eleitor():
    return render_template('eleitor.html')

@app.route('/escolha_seu_candidato', methods=['POST'])
def escolha_seu_candidato():
    data_form = request.form  
    session['eleitor'] = data_form['titulo_do_eleitor']
    import pprint;pprint.pprint(eleitor);
    return render_template('candidato.html')

@app.route('/confirma_candidato', methods=['POST'])
def confirma_candidato():
    data_form = request.form  
    session['candidato'] = data_form['candidato']
    import pprint;pprint.pprint(eleitor);pprint.pprint(candidato);  
    return render_template('confirma_candidato.html',
			   candidato=session['candidato'],
			   eleitor=session['eleitor'])

@app.route('/confirma_voto', methods=['POST'])
def confirma_voto():
    import datetime
#session['candidato'],
#session['eleitor']  
    from pymongo import MongoClient
    client = MongoClient()
    db = client.urna_eletronica_db
    collection = db.urna_eletronica_collection
    votacao = { 
    "titulo-eleitor": session['eleitor'],
    "candidato-escolhido": session['candidato'],
    "data-votacao": datetime.datetime.utcnow()
    }
    collection.insert_one(votacao).inserted_id
  
    return render_template('voto_confirmado.html',
			   eleitor=eleitor)

@app.route('/relatorio_votacao', methods=['GET'])
def relatorio_votacao():
    from pymongo import MongoClient
    client = MongoClient()
    db = client.urna_eletronica_db
    collection = db.urna_eletronica_collection
    danilo = collection.find({"candidato-escolhido": "danilo-gentili"}).count()
    carioca = collection.find({"candidato-escolhido": "carioca-panico"}).count()
    rafinha = collection.find({"candidato-escolhido": "rafinha-bastos"}).count()
    sergio = collection.find({"candidato-escolhido": "sergio-mallandro"}).count()
    total = (danilo + carioca + rafinha + sergio)
    import pprint;
    pprint.pprint(danilo);
    pprint.pprint(carioca);
    pprint.pprint(rafinha);
    pprint.pprint(sergio);
    pprint.pprint(total);
    return render_template('relatorio_votacao.html',
			   danilo=danilo,
			   carioca=carioca,
			   rafinha=rafinha,
			   sergio=sergio,
			   total=total)  
      
def obtem_mongodb():
    #MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True)
    return MongoClient("mongodb://localhost:27017")

if __name__ == '__main__'  :
    app.run()

