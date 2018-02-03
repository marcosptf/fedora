# -*- coding: utf-8 -*-
"""
este eh um server, para funcionar deve rodar:
python client-requests-put.py [enter]
"""

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

dados = {}

class HelloWord(Resource):
    def get(self, dados_id):
        return { dados_id : dados[dados_id] }

    def put(self, dados_id):
        dados[dados_id] = request.form['values']
        return { dados_id : dados[dados_id] }
    
api.add_resource(HelloWord, "/<string:dados_id>")

if __name__ == "__main__" :
    app.run(debug=True)


  
