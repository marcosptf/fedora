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

'''
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
app.config.update(dict( DEBUG=True, SECRET_KEY='sistema-de-urna-eletronica-key' ))

@app.route('/')
def index():
    ultima_senha = ultima_senha_chamada()
    ver_relatorio = ver_relatorio_paciente()
    return render_template('index_urna.html', 
			   ultima_senha = ultima_senha,
			   ver_relatorio = ver_relatorio)
  

@app.route('/identificacao_do_eleitor', methods=['POST'])
def identificacao_do_eleitor():
    return render_template('eleitor.html')


@app.route('/escolha_seu_candidato', methods=['POST'])
def escolha_seu_candidato():
    return render_template('candidato.html')


@app.route('/confirma_candidato', methods=['POST'])
def confirma_candidato():
    return render_template('confirma_candidato.html')

@app.route('/confirma_voto', methods=['POST'])
def confirma_voto():
    return render_template('voto_confirmado.html')

def ver_relatorio_paciente():
    conn = obtem_mariadb()
    try:
        with conn.cursor() as cursor:  
            query_relatorio_paciente = """
            select
            (select count(id) from painel where senha_atendida = '1') as pacientes_atendidos,

            (select count(id) from painel where senha_atendida = '0') as pacientes_aguardando_atendimento,

            (select count(id) from painel where senha_atendida = '0' and senha_prioridade = '1') as pacientes_prioridade_aguardando_atendimento;
            """
            cursor.execute(query_relatorio_paciente)
            return cursor.fetchone()  
            
    finally:
        conn.close()	  


def gera_proxima_senha_normal():
  
    conn = obtem_mariadb()
    try:
        with conn.cursor() as cursor:
            query_gera_senha_normal = """
            insert into painel
            (senha_prioridade, senha_atendida, ultima_senha_atendida)
            values
            (default, default, default);
            """
            cursor.execute(query_gera_senha_normal)
            conn.commit()
            flash('Senha Normal Gerada')            
            
    finally:
        conn.close()


def gera_proxima_senha_prioridade():
  
    conn = obtem_mariadb()
    try:
        with conn.cursor() as cursor:
            query_gera_senha_prioridade = """
            insert into painel
            (senha_prioridade, senha_atendida, ultima_senha_atendida)
            values
            (1, default, default);
            """
            cursor.execute(query_gera_senha_prioridade)
            conn.commit()
            flash('Senha Prioridade Gerada')            
            
    finally:
        conn.close()


def atende_proximo_paciente():
  
    relatorio = ver_relatorio_paciente()  
    
    if relatorio['pacientes_aguardando_atendimento'] > 0:
        conn = obtem_mariadb()
        try:
            with conn.cursor() as cursor:

                ultimo_paciente = ultima_senha_chamada()

                query_atendido = """
                update    painel 
                set       ultima_senha_atendida = '0'
                where     id = '%s';
                """
                cursor.execute(query_atendido, ultimo_paciente['id'])
                conn.commit()
            
                query_proximo_paciente = """
                select   id 
                from     painel 
                where    senha_atendida = '0'
                order by senha_prioridade desc,
	                 id asc
                limit    1;            
                """
                cursor.execute(query_proximo_paciente)
                resp_proximo_paciente =  cursor.fetchone()
            
                query_atualiza_painel = """
                update   painel
                set      ultima_senha_atendida = '1',
                         senha_atendida = '1'
                where    id = '%s';
                """
                cursor.execute(query_atualiza_painel, resp_proximo_paciente['id'])
                conn.commit()            
                flash('Chamando Proximo Paciente')

        finally:
            conn.close()


def ultima_senha_chamada():
  
    conn = obtem_mariadb()
    try:
        with conn.cursor() as cursor:
            sql = "select id from painel where ultima_senha_atendida = '1';"
            cursor.execute(sql)
            return cursor.fetchone()
    finally:
        conn.close()    

      
def obtem_mariadb():
    conn = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='sistema_de_espera',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    return conn
 

if __name__ == '__main__'  :
    app.run()

