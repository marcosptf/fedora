# -*- coding: utf-8 -*-
"""
este eh um server, para funcionar deve rodar:
python client-request-restFul.py runserver [enter]
"""

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

TODOS_CARROS = {
    'carro1': {'marca': 'fiat'},
    'carro2': {'marca': 'abarth'},
    'carro3': {'marca': 'lancia'},
}

def aborta_caso_carro_nao_exista(carro_id):
    if carro_id not in TODOS_CARROS:
        abort(404, message="Este carro {} nao existe ".format(carro_id))

parser = reqparse.RequestParser()
parser.add_argument('marca')

class Carros(Resource):

    def get(self, carro_id):
        if carro_id == "todos":
            return TODOS_CARROS

        aborta_caso_carro_nao_exista(carro_id)
        return TODOS_CARROS[carro_id]

    def delete(self, carro_id):
        aborta_caso_carro_nao_exista(carro_id)
        del TODOS_CARROS[carro_id]
        return '', 204

    def put(self, carro_id):
        args = parser.parse_args()
        marca = {'marca': args['marca']}
        TODOS_CARROS[carro_id] = marca
        return marca, 201

    def post(self, carro_id):
        aborta_caso_carro_nao_exista(carro_id)
        args = parser.parse_args()
        marca = {'marca': args['marca']}
        TODOS_CARROS[carro_id] = marca

    def head(self, carro_id):
        #pesquisar o tipo de retorno head para colocar aqui
        return {'code': 'error125', 'message': 'resource not found'}
    
    def options(self, carro_id):
        return {'methods': ['GET', 'HEAD', 'DELETE', 'POST', 'PUT', 'OPTIONS']}


## Actually setup the Api resource routing here
api.add_resource(Carros, '/marcas/<carro_id>')

if __name__ == '__main__':
    app.run(debug=True)



