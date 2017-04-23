# -*- coding: utf-8 -*-
"""
    sistema de contatos feito com sqlalchemy

http://docs.sqlalchemy.org/en/rel_1_1/intro.html
http://docs.sqlalchemy.org/en/rel_1_1/orm/index.html
http://docs.sqlalchemy.org/en/latest/core/engines.html
http://docs.sqlalchemy.org/en/rel_1_1/core/tutorial.html
http://docs.sqlalchemy.org/en/rel_1_1/orm/tutorial.html
http://docs.sqlalchemy.org/en/rel_1_1/orm/mapper_config.html
http://docs.sqlalchemy.org/en/rel_1_1/orm/relationships.html


import sqlalchemy
from sqlalchemy import create_engine
#engine = create_engine('postgresql://scott:tiger@localhost:5432/mydatabase')
engine = create_engine("mysql://root:123456@localhost:3306/sistema_de_contatos", echo=True)

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
import pymysql.cursors
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from sqlalchemy.orm import sessionmaker
from sqlalchemy_base import engine
from sqlalchemy_schema import Contatos

'''
Aqui é criado a aplicacao flask
'''
app = Flask(__name__)

'''
criando uma instancia de session
'''
Session = sessionmaker(bind=engine)
session = Session()

'''
Aqui é adicionado as configuracoes da aplicacao
'''
app.config.update(dict( DEBUG=True, SECRET_KEY='sistema-de-contatos-key' ))

@app.route('/')
def index():
    contatos = listar_contatos()
    return render_template('exibe_painel.html',
                           contatos=contatos)

@app.route('/editar_contato', methods=['GET'])
def editar_contato():
    data_form = request.form
    contatos = busca_contato(request.args.get('id'))
    return render_template('editar_contato.html',
                           contatos=contatos)

@app.route('/deletar_contato', methods=['GET'])
def deletar_contato():
    apaga_contato(request.args.get('id'))
    flash('contato deletado com sucesso!')
    return redirect(url_for('index'))

@app.route('/novo_contato', methods=['GET'])
def novo_contato():
    return render_template('novo_contato.html')

@app.route('/salva_contato', methods=['POST'])
def salva_contato():
    data_form = request.form 

    if data_form['contato_nome'] == "":
        flash('favor, coloque o nome do contato!')

    if data_form['voltar_index'] == "cancelar":
        return redirect(url_for('index'))

    salva_contato_query(data_form)
    return redirect(url_for('index'))

def apaga_contato(id):
    try:
        contato = session.query(Contatos).filter_by(id=id).first()
        session.delete(contato)
        session.commit()
    finally:
        pass

def busca_contato(id):
    try:
        return session.query(Contatos).filter_by(id=id).first()
    finally:
        pass
 
def salva_contato_query(data_form):

    try:
        if(data_form['id'] == "" ):
            add_novo_contato = Contatos(nome = data_form['nome'],
                                        email = data_form['email'],
                                        whatsapp = data_form['whatsapp'],
                                        facebook = data_form['facebook'],
                                        twitter = data_form['twitter'],
                                        website = data_form['website'],
                                        endereco = data_form['endereco'],
                                        bairro = data_form['bairro'],
                                        cidade = data_form['cidade'],
                                        estado = data_form['estado'],)
            session.add(add_novo_contato)
            session.commit()

        else:
            contato = session.query(Contatos).filter_by(id=data_form['id']).first()
            contato.nome = data_form['nome']
            contato.email = data_form['email']
            contato.whatsapp = data_form['whatsapp']
            contato.facebook = data_form['facebook']
            contato.twitter = data_form['twitter']
            contato.website = data_form['website']
            contato.endereco = data_form['endereco']
            contato.bairro = data_form['bairro']
            contato.cidade = data_form['cidade']
            contato.estado = data_form['estado']

            session.commit()

        flash('contato salvo com sucesso!')     
            
    finally:
        pass

def listar_contatos():
    try:
        return session.query(Contatos).order_by(Contatos.id)
            
    finally:
        pass

if __name__ == '__main__'  :
    app.run()

