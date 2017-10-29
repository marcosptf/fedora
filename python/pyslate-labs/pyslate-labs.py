# -*- coding: utf-8 -*-
#lib usada para este labs
#https://pypi.python.org/pypi/pyslate/1.1
from flask import Flask
app = Flask(__name__)
#>>> from pyslate.pyslate import Pyslate
#>>> from pyslate.backends.json_backend import JsonBackend
#>>> pys_en = Pyslate("en", backend=JsonBackend("translations.json"))
#>>> pys_en.translate("hello_world")
#Hello world!
#>>> pys_pl = Pyslate("pl", backend=JsonBackend("translations.json"))
#>>> pys_pl.translate("hello_world")
#Witaj świecie!

@app.route('/')
def ola_mundo():
    from pyslate.pyslate import Pyslate
    from pyslate.backends.json_backend import JsonBackend
    #para ingles
    pys_en = Pyslate("en", backend=JsonBackend("translations.json"))
    pys_en.translate("hello_world")
    #para polones
    pys_pl = Pyslate("pl", backend=JsonBackend("translations.json"))
    pys_pl.translate("hello_world")
    
    return 'aplicacao flask python translate ==> %s' % pys_en.translate("hello_world")
  
if __name__ == '__main__'  :
    app.run()

