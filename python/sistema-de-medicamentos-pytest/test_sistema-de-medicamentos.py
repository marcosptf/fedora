# -*- coding: utf-8 -*-
"""
pytest sistema de medicamentos
"""

from sistema_de_medicamentos import listar_medicamentos 

class TestClass:

    def test_retorna_medicamento_doril(self):
        lista = listar_medicamentos()
        assert_doril = "doril"

        assert assert_doril in lista['medicamento'][0]['nome']

    def test_retorna_medicamento_generico(self):
        generico = []
        assert_lista_genericos = ['resfenol', 'paracetamol', 'multigrip']
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['generico']=="True":
                generico.append(medicamento['nome'])
        
        assert assert_lista_genericos == generico

    def test_retorna_medicamento_desconto_gestante(self):
        gestante = []
        assert_lista_gestante = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol']
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['desconto-gestantes'] == "True":
                gestante.append(medicamento['nome'])

        assert assert_lista_gestante == gestante

    def test_retorna_medicamento_desconto_aposentado(self):
        aposentado = []
        assert_lista_aposentado = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip']
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['desconto-aposentados'] == "True":
                aposentado.append(medicamento['nome'])

        assert assert_lista_aposentado == aposentado
   

    def test_retorna_medicamento_farmacia_popular(self):
        farmacia_popular = []
        assert_lista_farmacia_popular = ['doril', 'buscopan', 'paracetamol']
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['farmacia-popular'] == "True":
                farmacia_popular.append(medicamento['nome'])

        assert assert_lista_farmacia_popular == farmacia_popular

    def test_retorna_medicamento_quantidade_comprimidos(self):
        quantidade_comprimidos = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip']
        assert_quantidade_comprimidos = 120
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras:
                quantidade_comprimidos += medicamento['quantidade-comprimidos']

        assert assert_quantidade_comprimidos == quantidade_comprimidos

    def test_retorna_medicamento_quantidade_comprimidos_nao_genericos(self):
        quantidade_comprimidos = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip']
        assert_quantidade_comprimidos = 70
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False":
                quantidade_comprimidos += medicamento['quantidade-comprimidos']

        assert assert_quantidade_comprimidos == quantidade_comprimidos

    def test_retorna_medicamento_quantidade_comprimidos_genericos_com_desconto_para_aposentados(self):
        quantidade_comprimidos = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_quantidade_comprimidos = 50
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="True" and medicamento['desconto-aposentados']=="True":
                quantidade_comprimidos += medicamento['quantidade-comprimidos']

        assert assert_quantidade_comprimidos == quantidade_comprimidos

    def test_retorna_medicamento_quantidade_comprimidos_genericos_com_desconto_para_gestantes(self):
        quantidade_comprimidos = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_quantidade_comprimidos = 30
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="True" and medicamento['desconto-gestantes']=="True":
                quantidade_comprimidos += medicamento['quantidade-comprimidos']

        assert assert_quantidade_comprimidos == quantidade_comprimidos

    def test_retorna_medicamento_quantidade_comprimidos_nao_genericos_com_desconto_para_aposentados(self):
        quantidade_comprimidos = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_quantidade_comprimidos = 70
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['desconto-aposentados']=="True":
                quantidade_comprimidos += medicamento['quantidade-comprimidos']

        assert assert_quantidade_comprimidos == quantidade_comprimidos

    def test_retorna_medicamento_quantidade_comprimidos_nao_genericos_com_desconto_para_gestantes(self):
        quantidade_comprimidos = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_quantidade_comprimidos = 70
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['desconto-gestantes']=="True":
                quantidade_comprimidos += medicamento['quantidade-comprimidos']

        assert assert_quantidade_comprimidos == quantidade_comprimidos

    def test_retorna_medicamento_preco_lista_de_compras(self):
        preco_medicamentos = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip']
        assert_preco_medicamentos = 31.5
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras:
                preco_medicamentos += medicamento['preco']

        assert assert_preco_medicamentos == preco_medicamentos

    def test_retorna_medicamento_preco_nao_genericos(self):
        preco = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip']
        assert_preco = 16.5
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False":
                preco += medicamento['preco']

        assert assert_preco == preco

    def test_retorna_medicamento_preco_genericos_com_desconto_para_aposentados(self):
        preco = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_preco = 15.0
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="True" and medicamento['desconto-aposentados']=="True":
                preco += medicamento['preco']

        assert assert_preco == preco

    def test_retorna_medicamento_preco_genericos_com_desconto_para_gestantes(self):
        preco = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_preco = 8.5
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="True" and medicamento['desconto-gestantes']=="True":
                preco += medicamento['preco']

        assert assert_preco == preco

    def test_retorna_medicamento_preco_nao_genericos_com_desconto_para_aposentados(self):
        preco = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_preco = 16.5
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['desconto-aposentados']=="True":
                preco += medicamento['preco']

        assert assert_preco == preco

    def test_retorna_medicamento_preco_nao_genericos_com_desconto_para_gestantes(self):
        preco = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_preco = 16.5
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['desconto-gestantes']=="True":
                preco += medicamento['preco']

        assert assert_preco == preco
        
    def test_retorna_medicamento_quantidade_comprimidos_nao_genericos_com_farmacia_popular(self):
        quantidade_comprimidos = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip']
        assert_quantidade_comprimidos = 40
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['farmacia-popular'] == "True":
                quantidade_comprimidos += medicamento['quantidade-comprimidos']

        assert assert_quantidade_comprimidos == quantidade_comprimidos

    def test_retorna_medicamento_quantidade_comprimidos_genericos_com_desconto_para_aposentados_com_farmacia_popular(self):
        quantidade_comprimidos = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_quantidade_comprimidos = 20
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="True" and medicamento['desconto-aposentados']=="True" and medicamento['farmacia-popular'] == "True":
                quantidade_comprimidos += medicamento['quantidade-comprimidos']

        assert assert_quantidade_comprimidos == quantidade_comprimidos

    def test_retorna_medicamento_quantidade_comprimidos_genericos_com_desconto_para_gestantes_com_farmacia_popular(self):
        quantidade_comprimidos = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_quantidade_comprimidos = 20
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="True" and medicamento['desconto-gestantes']=="True" and medicamento['farmacia-popular'] == "True":
                quantidade_comprimidos += medicamento['quantidade-comprimidos']

        assert assert_quantidade_comprimidos == quantidade_comprimidos

    def test_retorna_medicamento_quantidade_comprimidos_nao_genericos_com_desconto_para_aposentados_com_farmacia_popular(self):
        quantidade_comprimidos = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_quantidade_comprimidos = 40
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['desconto-aposentados']=="True" and medicamento['farmacia-popular'] == "True":
                quantidade_comprimidos += medicamento['quantidade-comprimidos']

        assert assert_quantidade_comprimidos == quantidade_comprimidos

    def test_retorna_medicamento_quantidade_comprimidos_nao_genericos_com_desconto_para_gestantes_com_farmacia_popular(self):
        quantidade_comprimidos = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_quantidade_comprimidos = 40
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['desconto-gestantes']=="True" and medicamento['farmacia-popular'] == "True":
                quantidade_comprimidos += medicamento['quantidade-comprimidos']

        assert assert_quantidade_comprimidos == quantidade_comprimidos

    def test_retorna_medicamento_preco_lista_de_compras_com_farmacia_popular(self):
        preco_medicamentos = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip']
        assert_preco_medicamentos = 13.5
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['farmacia-popular'] == "True":
                preco_medicamentos += medicamento['preco']

        assert assert_preco_medicamentos == preco_medicamentos

    def test_retorna_medicamento_preco_nao_genericos_com_farmacia_popular(self):
        preco = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip']
        assert_preco = 9.0
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['farmacia-popular'] == "True":
                preco += medicamento['preco']

        assert assert_preco == preco

    def test_retorna_medicamento_preco_genericos_com_desconto_para_aposentados_com_farmacia_popular(self):
        preco = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_preco = 4.5
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="True" and medicamento['desconto-aposentados']=="True" and medicamento['farmacia-popular'] == "True":
                preco += medicamento['preco']

        assert assert_preco == preco

    def test_retorna_medicamento_preco_genericos_com_desconto_para_gestantes_com_farmacia_popular(self):
        preco = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_preco = 4.5
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="True" and medicamento['desconto-gestantes']=="True" and medicamento['farmacia-popular'] == "True":
                preco += medicamento['preco']

        assert assert_preco == preco

    def test_retorna_medicamento_preco_nao_genericos_com_desconto_para_aposentados_com_farmacia_popular(self):
        preco = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_preco = 9.0
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['desconto-aposentados']=="True" and medicamento['farmacia-popular'] == "True":
                preco += medicamento['preco']

        assert assert_preco == preco

    def test_retorna_medicamento_preco_nao_genericos_com_desconto_para_gestantes_com_farmacia_popular(self):
        preco = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_preco = 9.0
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['desconto-gestantes']=="True" and medicamento['farmacia-popular'] == "True":
                preco += medicamento['preco']

        assert assert_preco == preco
      
    def test_retorna_medicamento_quantidade_comprimidos_nao_genericos_sem_farmacia_popular(self):
        quantidade_comprimidos = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip']
        assert_quantidade_comprimidos = 30
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['farmacia-popular'] == "False":
                quantidade_comprimidos += medicamento['quantidade-comprimidos']

        assert assert_quantidade_comprimidos == quantidade_comprimidos

    def test_retorna_medicamento_quantidade_comprimidos_genericos_com_desconto_para_aposentados_sem_farmacia_popular(self):
        quantidade_comprimidos = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_quantidade_comprimidos = 30
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="True" and medicamento['desconto-aposentados']=="True" and medicamento['farmacia-popular'] == "False":
                quantidade_comprimidos += medicamento['quantidade-comprimidos']

        assert assert_quantidade_comprimidos == quantidade_comprimidos

    def test_retorna_medicamento_quantidade_comprimidos_genericos_com_desconto_para_gestantes_sem_farmacia_popular(self):
        quantidade_comprimidos = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_quantidade_comprimidos = 10
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="True" and medicamento['desconto-gestantes']=="True" and medicamento['farmacia-popular'] == "False":
                quantidade_comprimidos += medicamento['quantidade-comprimidos']

        assert assert_quantidade_comprimidos == quantidade_comprimidos

    def test_retorna_medicamento_quantidade_comprimidos_nao_genericos_com_desconto_para_aposentados_sem_farmacia_popular(self):
        quantidade_comprimidos = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_quantidade_comprimidos = 30
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['desconto-aposentados']=="True" and medicamento['farmacia-popular'] == "False":
                quantidade_comprimidos += medicamento['quantidade-comprimidos']

        assert assert_quantidade_comprimidos == quantidade_comprimidos

    def test_retorna_medicamento_quantidade_comprimidos_nao_genericos_com_desconto_para_gestantes_sem_farmacia_popular(self):
        quantidade_comprimidos = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_quantidade_comprimidos = 30
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['desconto-gestantes']=="True" and medicamento['farmacia-popular'] == "False":
                quantidade_comprimidos += medicamento['quantidade-comprimidos']

        assert assert_quantidade_comprimidos == quantidade_comprimidos

    def test_retorna_medicamento_preco_lista_de_compras_sem_farmacia_popular(self):
        preco_medicamentos = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip']
        assert_preco_medicamentos = 18.0
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['farmacia-popular'] == "False":
                preco_medicamentos += medicamento['preco']

        assert assert_preco_medicamentos == preco_medicamentos

    def test_retorna_medicamento_preco_nao_genericos_sem_farmacia_popular(self):
        preco = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip']
        assert_preco = 7.5
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['farmacia-popular'] == "False":
                preco += medicamento['preco']

        assert assert_preco == preco

    def test_retorna_medicamento_preco_genericos_com_desconto_para_aposentados_sem_farmacia_popular(self):
        preco = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_preco = 10.5
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="True" and medicamento['desconto-aposentados']=="True" and medicamento['farmacia-popular'] == "False":
                preco += medicamento['preco']

        assert assert_preco == preco

    def test_retorna_medicamento_preco_genericos_com_desconto_para_gestantes_sem_farmacia_popular(self):
        preco = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_preco = 4.0
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="True" and medicamento['desconto-gestantes']=="True" and medicamento['farmacia-popular'] == "False":
                preco += medicamento['preco']

        assert assert_preco == preco

    def test_retorna_medicamento_preco_nao_genericos_com_desconto_para_aposentados_sem_farmacia_popular(self):
        preco = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_preco = 7.5
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['desconto-aposentados']=="True" and medicamento['farmacia-popular'] == "False":
                preco += medicamento['preco']

        assert assert_preco == preco

    def test_retorna_medicamento_preco_nao_genericos_com_desconto_para_gestantes_sem_farmacia_popular(self):
        preco = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_preco = 7.5
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['desconto-gestantes']=="True" and medicamento['farmacia-popular'] == "False":
                preco += medicamento['preco']

        assert assert_preco == preco

    def test_retorna_medicamento_preco_genericos_com_desconto_para_gestantes_com_desconto_aposentado_com_farmacia_popular(self):
        preco = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_preco = 4.5
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="True" and medicamento['desconto-gestantes']=="True" and medicamento['desconto-aposentados']=="True"  and medicamento['farmacia-popular'] == "True":
                preco += medicamento['preco']

        assert assert_preco == preco

    def test_retorna_medicamento_preco_nao_genericos_sem_desconto_para_gestantes_sem_desconto_aposentado_sem_farmacia_popular(self):
        preco = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_preco = 3.0
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['desconto-gestantes']=="False" and medicamento['desconto-aposentados']=="False" and medicamento['farmacia-popular'] == "False":
                preco += medicamento['preco']

        assert assert_preco == preco

    def test_retorna_medicamento_preco_nao_genericos_sem_desconto_para_gestantes_sem_desconto_aposentado_sem_farmacia_popular_quantidade_miligramas_200mg(self):
        preco = 0
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_preco = 3.0
        lista = listar_medicamentos()

        for medicamento in lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['desconto-gestantes']=="False" and medicamento['desconto-aposentados']=="False" and medicamento['farmacia-popular'] == "False" and medicamento['miligramas'] == "200mg":
                preco += medicamento['preco']

        assert assert_preco == preco













