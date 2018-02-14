from suds.client import Client as SudsClient
import requests

url = 'http://127.0.0.1:5000/soap/someservicetwo?wsdl'
client = SudsClient(url=url, cache=None)

todos_medicamentos = client.service.todos_medicamentos()
doril_medicamento = client.service.medicamento_preco('Doril')
medicamento_errado = client.service.medicamento_preco('joril')

print("todos medicamentos:")
print(todos_medicamentos)
print("preco do doril:")
print(doril_medicamento)
print("medicamento errado:")
print(medicamento_errado)
print("")
