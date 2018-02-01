from suds.client import Client as SudsClient
import requests

url = 'http://127.0.0.1:5000/soap/someservicetwo?wsdl'
client = SudsClient(url=url, cache=None)
#r = client.service.echo(str='hello world', cnt=3)
#print(r)

#r = client.service.answer(str='some question')
#print(r)

#r = client.service.todos_medicamentos()
#r = client.service.medicamento_preco('Doril')
r = client.service.medicamento_preco('joril')
print(r)

