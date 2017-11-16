# -*- coding: utf-8 -*-
import requests

print("\n")
print("obtendo dados da api-server-restFul =>")

endpoint = "http://127.0.0.1:5000/marcas/"
todos_carros = "todos"

def resposta_request(resp):
    print("status-code:")
    print(resp.status_code)
    print("headers:")
    print(resp.headers['content-type'])
    print("json:")
    print(resp.json())
    print("\n")

rq = requests.get(endpoint + todos_carros)
resposta_request(rq)

print("enviando request put => marca:alfa-romeo ")
requests.put(endpoint + "carro4", data={"marca" : "alfa-romeo" })
print("\n")

print("obtendo dados da api-server-restFul =>")
rq = requests.get(endpoint + todos_carros)
resposta_request(rq)

print("obtendo dados da api-server-restFul => somente o alfa-romeo")
rq = requests.get(endpoint + "carro4")
resposta_request(rq)

print("obtendo dados da api-server-restFul => buscando um carro que nao existe")
rq = requests.get(endpoint + "carro5")
resposta_request(rq)

print("enviando request post => marca:alfa-romeo ==> marca:maseratti ")
requests.post(endpoint + "carro4", data={"marca" : "maseratti" })
print("\n")

print("obtendo dados da api-server-restFul =>")
rq = requests.get(endpoint + todos_carros)
resposta_request(rq)

print("enviando request delete => task:maseratti")
requests.delete(endpoint + "carro4")
print("\n")


print("obtendo dados da api-server-restFul =>")
rq = requests.get(endpoint + todos_carros)
resposta_request(rq)
print("\n")


print("enviando request head =>")
rq = requests.head(endpoint + "carro4")
print(rq.headers['content-type'])
print("\n")


print("enviando request options =>")
rq = requests.options(endpoint + "carro4")
resposta_request(rq)

