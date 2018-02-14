#from flask import Flask
#from flask_graphql import GraphQLView
import json
from flask import url_for
import urllib3

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

def url_string(**url_params):
    string = url_for('http://127.0.0.1/graphql')
    if url_params:
        string += '?' + urlencode(url_params)
    return string

def response_json(response):
    return json.loads(response.data.decode())

http = urllib3.PoolManager()
http_respose = http.request("GET", "http://127.0.0.1:5000/graphql?query={test}")
print(http_respose.data)
#print(response_json(http_respose.data))
#assert response_json(response) == {
#    'data': {'test': "Hello World"}
#}




