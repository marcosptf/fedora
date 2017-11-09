# -*- coding: utf-8 -*-
"""
este eh um server, para funcionar deve rodar:
python client-requests-get.py [enter]
"""

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWord(Resource):
    def get(self):
        return { "hello" : "word" }
    
api.add_resource(HelloWord, "/")

if __name__ == "__main__" :
    app.run(debug=True)


  
