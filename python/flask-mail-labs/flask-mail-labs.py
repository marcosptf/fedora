# -*- coding: utf-8 -*-
"""
Flask mail
https://pythonhosted.org/Flask-Mail/
https://github.com/mattupstate/flask-mail

#pendencias
1.fazer tela para preencher dados para enviar no email
2.fazer tela para receber estes dados e responder como enviado com sucesso ou erro

"""
from flask import Flask
from flask_mail import Mail, Message

'''
Aqui é criado a aplicacao flask
'''
app = Flask(__name__)
mail = Mail(app)

'''
Aqui é adicionado as configuracoes da aplicacao
'''
app.config.update(dict( DEBUG=True, SECRET_KEY='sistema-de-espera-key' ))
mail.init_app(app)


@app.route('/')
def index():
    ultima_senha = ultima_senha_chamada()
    ver_relatorio = ver_relatorio_paciente()
    return render_template('exibe_painel.html', 
			   ultima_senha = ultima_senha,
			   ver_relatorio = ver_relatorio)
  

@app.route('/menu_senha', methods=['POST'])
def menu_senha():
  
    tipo_menu = request.form
    if 'gera_proxima_senha' in tipo_menu:
        gera_proxima_senha_normal()

    if 'gera_proxima_senha_prioridade' in tipo_menu: 
        gera_proxima_senha_prioridade()

    if 'atende_proximo_paciente' in tipo_menu: 
        atende_proximo_paciente()

    return redirect(url_for('index'))

def envia_email():
    msg = Message("Hello", sender="from@example.com", recipients=["to@example.com"])
#   msg.recipients = ["you@example.com"]
#   msg.add_recipient("somebodyelse@example.com")
msg = Message("Hello", sender=("Me", "me@example.com"))
assert msg.sender == "Me <me@example.com>"
#msg.body = "testing"
msg.html = "<b>testing</b>"

"""
#example send lt mails
#The connection to your email host is kept alive and closed automatically once all the messages have been sent.
with mail.connect() as conn:
    for user in users:
        message = '...'
        subject = "hello, %s" % user.name
        msg = Message(recipients=[user.email],
                      body=message,
                      subject=subject)

        conn.send(msg)

#enviando anexos
with app.open_resource("image.png") as fp:
    msg.attach("image.png", "image/png", fp.read())
"""

if __name__ == '__main__'  :
    app.run()

