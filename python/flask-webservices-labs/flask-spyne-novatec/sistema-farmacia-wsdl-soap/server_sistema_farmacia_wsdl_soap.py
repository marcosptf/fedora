from flask import Flask
from flask_spyne import Spyne
from spyne.protocol.http import HttpRpc
from spyne.protocol.soap import Soap11
from spyne.model.primitive import Unicode, Integer
from spyne.model.complex import Iterable, ComplexModel
import logging

h = logging.StreamHandler()
rl = logging.getLogger()
rl.setLevel(logging.DEBUG)
rl.addHandler(h)

app = Flask(__name__)
spyne = Spyne(app)

class AnswerServiceResponse(ComplexModel):
    __namespace__ = 'tns'
    dummy_str = Unicode(min_occurs=0, max_occurs=1, nillable=True)
    dummy_num = Integer(min_occurs=1, max_occurs=1, nillable=True)
    medicamentos = Unicode(min_occurs=0, max_occurs=1, nillable=False)

class SomeSoapServiceTwo(spyne.Service):
    __service_url_path__ = '/soap/someservicetwo'
    __target_namespace__ = 'custom_namespacetwo'
    __in_protocol__ = Soap11(validator='lxml')
    __out_protocol__ = Soap11()

    @spyne.srpc(_returns=Iterable(Unicode))
    #@spyne.srpc(_returns=AnswerServiceResponse)
    def todos_medicamentos():
        medicamentos_tabela = {
            "Doril" : "1,99",
            "Novalgina" : "1,99",
            "Paracetamol" : "1,99",
            "Buscopan" : "1,99",
            "Dorflex" : "1,99"
        }

        for i in AnswerServiceResponse(medicamentos=medicamentos_tabela):
            yield medicamentos_tabela
        #return AnswerServiceResponse(medicamentos=medicamentos_tabela)

    @spyne.srpc(Unicode, Integer, _returns=Iterable(Unicode))
    def echo(str, cnt):
        for i in range(cnt):
            yield str

    @spyne.srpc(Unicode, _returns=AnswerServiceResponse)
    def answer(str):
        print(str)
        return AnswerServiceResponse(dummy_str='answer is', dummy_num=42)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
