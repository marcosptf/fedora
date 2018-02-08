"""
tentando obter o ultimo resultado da mega sena

http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena//
"""

import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

url_scrapy = "http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/"

body = '<html><body><span>good</span></body></html>'
Selector(text=body).xpath('//span/text()').extract()

response = HtmlResponse(url=url_scrapy, body=body)
Selector(response=response).xpath('//span/text()').extract()
#[u'good']

