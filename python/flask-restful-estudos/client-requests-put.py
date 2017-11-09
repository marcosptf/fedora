"""
este eh um client, para funcionar deve rodar:
python api-server-put.py runserver [enter]
"""

#from requests import get, put
import requests

requests.put("http://127.0.0.1:5000/dados_1", data={"values" : "valor1" }).json()
rq = requests.get("http://127.0.0.1:5000/dados_1")
print("status-code:")
print(rq.status_code)
print("headers:")
print(rq.headers['content-type'])
print("text:")
print(rq.text)
print("json:")
print(rq.json())
print("\n\n")

requests.put("http://127.0.0.1:5000/dados_2", data={"values" : "valor2" }).json()
rq = requests.get("http://127.0.0.1:5000/dados_2")
print("status-code:")
print(rq.status_code)
print("headers:")
print(rq.headers['content-type'])
print("text:")
print(rq.text)
print("json:")
print(rq.json())
