"""
este eh um client, para funcionar deve rodar:
python api-server-get.py runserver [enter]
"""

import requests

endpoint = "http://127.0.0.1:5000"
rq = requests.get(endpoint)

print("status-code:")
print(rq.status_code)
print("headers:")
print(rq.headers['content-type'])
print("text:")
print(rq.text)
print("json:")
print(rq.json())