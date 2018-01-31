from flask import Flask
from flask_spyne import Spyne
from spyne.protocol.http import HttpRpc
from spyne.protocol.json import JsonDocument
from spyne.model.primitive import Unicode, Integer
from spyne.model.complex import Iterable, ComplexModel
import logging

h = logging.StreamHandler()
rl = logging.getLogger()
rl.setLevel(logging.DEBUG)
rl.addHandler(h)

app = Flask(__name__)
spyne = Spyne(app)

class SomeJsonService(spyne.Service):
    __service_url_path__ = '/json/anotherservice'
    __in_protocol__ = HttpRpc(validator='soft')
    __out_protocol__ = JsonDocument(ignore_wrappers=True)

    @spyne.srpc(Unicode, Integer, _returns=Iterable(Unicode))
    def echo(str, cnt):
        for i in range(cnt):
            yield str

if __name__ == '__main__':
    app.run(host='0.0.0.0')
