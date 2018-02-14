from suds.client import Client as SudsClient
import requests

#get via browser =>
#http://127.0.0.1:5000/json/anotherservice/echo?str=java&cnt=4
url = 'http://127.0.0.1:5000/json/anotherservice/echo'
params = {'str': 'hello world', 'cnt': 3}
r = requests.get(url=url, params=params)
print(r.text)

