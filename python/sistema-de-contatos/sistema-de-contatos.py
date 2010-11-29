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
app.config.update(dict( DEBUG=True, SECRET_KEY='sistema-de-contatos-key' ))

@app.route('/')
def index():
    print("===>>>>index");  
    conn = obtem_mariadb()    
    import pprint;pprint.pprint(conn);
    return render_template('exibe_painel.html')
  

@app.route('/novo_contato', methods=['GET'])
def novo_contato():
    print("===>>>>novo contato");
    return render_template('novo_contato.html')

@app.route('/salva_contato', methods=['POST'])
def salva_contato():
    conn = obtem_mariadb()    
    print("func===>>>1")
    try:
	data_form = request.form 
	print("func===>>>2")
	import pprint;pprint.pprint(data_form);
	print("func===>>>3")
	if data_form['contato_nome'] == "":
	    flash('favor, coloque o nome do contato!')
	print("func===>>>4")  
	if data_form['voltar_index'] == "cancelar":
	    return render_template('exibe_painel.html')

        print("func===>>>5")
        with conn.cursor() as cursor:
	    
	    print("\n\n")
            print("query===>>>")
            query_insere_novo_contato = "
            insert into painel
            (nome,email,whatsapp,facebook,twitter,website,endereco,bairro,cidade,estado)
            values
            (
            '"+data_form['contato_nome']+"',
            '"+data_form['contato_email']+"',
            '"+data_form['contato_whatsapp']+"',
            '"+data_form['contato_facebook']+"',            
            '"+data_form['contato_twitter']+"',
            '"+data_form['contato_website']+"',
            '"+data_form['contato_endereco']+"',
            '"+data_form['contato_bairro']+"',
            '"+data_form['contato_cidade']+"',
            '"+data_form['contato_nome']+"'"
            import pprint;pprint.pprint(query_insere_novo_contato);
            print("\n\n\n")
            print(query_insere_novo_contato)
            
	    cursor.execute(query_insere_novo_contato)
            conn.commit()
            flash('novo contato salvo com sucesso!')     
            
    finally:
        conn.close()

    return render_template('novo_contato.html')    

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
                             db='sistema_de_contatos',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    return conn
 

if __name__ == '__main__'  :
    app.run()

