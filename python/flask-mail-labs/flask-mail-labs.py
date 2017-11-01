# -*- coding: utf-8 -*-
"""
Flask mail
https://pythonhosted.org/Flask-Mail/
https://github.com/mattupstate/flask-mail

#pendencias
1.fazer tela para preencher dados para enviar no email
2.fazer tela para receber estes dados e responder como enviado com sucesso ou erro

"""
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask_mail import Mail, Message

'''
Aqui é criado a aplicacao flask
'''
app = Flask(__name__)
mail = Mail(app)

'''
Aqui é adicionado as configuracoes da aplicacao
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT='587'
    MAIL_USE_TLS=True
    MAIL_USE_SSL=True
    MAIL_USERNAME=''
    MAIL_PASSWORD=''
    MAIL_DEBUG : default app.debug
    MAIL_DEFAULT_SENDER : default None
    MAIL_MAX_EMAILS : default None
    MAIL_SUPPRESS_SEND : default app.testing
    MAIL_ASCII_ATTACHMENTS : default False
'''

app.config.update(dict(DEBUG=True, SECRET_KEY='sistema-de-espera-key',
                MAIL_SERVER='smtp.gmail.com', MAIL_PORT='587',
				MAIL_USE_TLS=True, MAIL_USE_SSL=True, 
				MAIL_USERNAME='', MAIL_PASSWORD=''))
mail.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    #envia_email(request.form)
	msg = Message("assunto do email", sender="marcosptf@yahoo.com.br", 
                recipients="marcos.santana@fs.com.br", body="texto do email")
	mail.send(msg)
    return render_template('exibe_painel.html')

"""
def envia_email(email_form):
    msg = Message(email_form['email_assunto'], sender="marcosptf@yahoo.com.br", recipients=email_form['email_para'])
    msg.recipients = ["you@example.com"]
    msg.add_recipient(email_form['email_com_copia'])
    msg.body = email_form['email_mensagem']
    #msg.html = "<b>testing</b>"
    #msg = Message("Hello", sender=("Me", "me@example.com"))
    #with app.open_resource(email_form['email_anexo']) as fp:
    #    msg.attach(email_form['email_anexo'], "image/png", fp.read())	
	
	mail.send(msg)

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

