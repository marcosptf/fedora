# -*- coding: utf-8 -*-
"""
pytest sistema de medicamentos
"""

from sistema_de_medicamentos import listar_medicamentos 

class TestClass:

    def test_one(self):
        assert "java"

    def test_retorna_medicamento_doril(self):
        listar = listar_medicamentos()
        assert "doril" in listar['medicamento'][0]['nome']

    def test_retorna_medicamento_generico(self):
        generico = []
        listar = listar_medicamentos()

        for medicamento in listar['medicamento']:
            if medicamento['generico']=="True":
                generico.append(medicamento['nome'])
        
        #assert 'resfenol', 'paracetamol', 'multigrip' in generico
        assert 'resfenol' in generico

                  
        
