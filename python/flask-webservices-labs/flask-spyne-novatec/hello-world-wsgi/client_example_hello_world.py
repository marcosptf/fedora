from suds.client import Client as SudsClient
import requests

print("request wsdl")
url = 'http://localhost:7789/?wsdl'
print(url)
client = SudsClient(url=url, cache=None)
resp_request = client.service.say_hello(name='hello world', times=7)
print(resp_request)

