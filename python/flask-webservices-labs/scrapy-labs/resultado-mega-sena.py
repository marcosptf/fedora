"""
tentando obter o ultimo resultado da mega sena

http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena//
"""

import scrapy


class BlogSpider(scrapy.Spider):
    name = 'mega-sena'
    start_urls = ['http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/']

    def parse(self, response):
        print("inside-function===>>>")
        print("response====>>>")
        print(response)
        dir(response)
        print("response.css====>>>>")
        print(response.css('ul#ulDezenas::text').extract())
        for li in response.css('ul#ulDezenas::text'):
	    print("inside-interator====>>>>")
            print(li.extract())
            #yield {'li' : li.css}
            #yield response.follow(li, self.parse)
            #yield {'li': li.css('li').extract_first()}


 