# -*- coding: utf-8 -*-
"""
Flask paramiko
http://www.sftp.net/public-online-sftp-servers

"""
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import base64
import getpass
import os
import socket
import sys
import traceback
from paramiko.py3compat import input
import paramiko

'''
Aqui é criado a aplicacao flask
'''
app = Flask(__name__)

# setup logging
paramiko.util.log_to_file('demo_simple.log')
# Paramiko client configuration
# enable "gssapi-with-mic" authentication, if supported by your python installation
UseGSSAPI = paramiko.GSS_AUTH_AVAILABLE
# enable "gssapi-kex" key exchange, if supported by your python installation
DoGSSAPIKeyExchange = paramiko.GSS_AUTH_AVAILABLE
UseGSSAPI = True             # enable GSS-API / SSPI authentication
DoGSSAPIKeyExchange = True
port = 22
username = 'demo'
hostname = 'test.rebex.net'
password = 'password'

# now, connect and use paramiko Client to negotiate SSH2 across the connection
try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy())
	
    print("py=>1")
    if not UseGSSAPI and not DoGSSAPIKeyExchange:
        print("py=>2")
        client.connect(hostname, port, username, password)
    else:
        print("py=>3")
        try:
            print("py=>4")
            client.connect(hostname, port, username, gss_auth=UseGSSAPI, gss_kex=DoGSSAPIKeyExchange)
        except Exception:
            print("py=>5")
            password = getpass.getpass('Password for %s@%s: ' % (username, hostname))
            client.connect(hostname, port, username, password)

    stdin, stdout, stderr = client.exec_command('ls -lart')
    #dirlist = client.listdir(".")
    print("list====>>>")
    for line in stdout:
        print(line.strip('\n'))

    client.close()

except Exception as e:
    print('*** Caught exception: %s: %s' % (e.__class__, e))
    traceback.print_exc()
    try:
        client.close()
    except:
        pass


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('exibe_painel.html')
	
	
if __name__ == '__main__'  :
    app.run()
