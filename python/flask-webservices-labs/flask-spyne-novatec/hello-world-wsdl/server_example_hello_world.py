from flask import Flask
from flask_spyne import Spyne
from spyne.protocol.http import HttpRpc
from spyne.protocol.soap import Soap11
from spyne.model.primitive import Unicode, Integer
from spyne.model.complex import Iterable, ComplexModel
import logging
#http://127.0.0.1:5000/soap/helloworldservice?wsdl
h = logging.StreamHandler()
rl = logging.getLogger()
rl.setLevel(logging.DEBUG)
rl.addHandler(h)

app = Flask(__name__)
spyne = Spyne(app)

class SoapServiceHelloWorld(spyne.Service):
    __service_url_path__ = '/soap/helloworldservice'
    __in_protocol__ = Soap11(validator='lxml')
    __out_protocol__ = Soap11()

    @spyne.srpc(Unicode, Integer, _returns=Iterable(Unicode))
    def method_hello_world(str, cnt):
        for i in range(cnt):
            yield str

if __name__ == '__main__':
    app.run(host='0.0.0.0')
