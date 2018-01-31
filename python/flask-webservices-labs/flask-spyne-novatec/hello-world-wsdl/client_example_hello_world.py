from suds.client import Client as SudsClient
import requests

print("request wsdl")
url = 'http://127.0.0.1:5000/soap/helloworldservice?wsdl'
print(url)
client = SudsClient(url=url, cache=None)
resp_request = client.service.method_hello_world(str='hello world', cnt=7)
print(resp_request)

