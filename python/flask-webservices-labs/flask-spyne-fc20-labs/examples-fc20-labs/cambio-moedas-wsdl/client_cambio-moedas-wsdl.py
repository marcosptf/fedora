from suds.client import Client as SudsClient
import requests

print("request wsdl")
url = 'http://www.webservicex.com/CurrencyConvertor.asmx?wsdl'
print(url)
client = SudsClient(url=url, cache=None)
resp_request = client.service.ConversionRate(FromCurrency='BRL', ToCurrency='GBP')
print(resp_request)

