# -*- coding: utf-8 -*-
"""
pytest sistema de medicamentos
"""

from lista_medicamentos_json import medicamento
from sistema_medicamentos_class import SistemaMedicamento

class MedicamentoClass:
    def __init__(self):
        med = medicamento()
        self.lista = med.lista_medicamentos_json()  
        self.sistema = SistemaMedicamento()

class TestClass():
    def test_retorna_medicamento_doril(self):
        med = MedicamentoClass()
        assert med.sistema.medicamento_doril() in med.lista['medicamento'][0]['nome']

    def test_retorna_medicamento_generico(self):
        generico = []
        med = MedicamentoClass()
        assert_medicamento_generico = ['resfenol', 'paracetamol', 'multigrip']
        assert med.sistema.medicamento_generico() == assert_medicamento_generico

    def test_retorna_medicamento_desconto_gestante(self):
        med = MedicamentoClass()
        assert_medicamento_desconto_gestante = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol']
        assert med.sistema.medicamento_desconto_gestante() == assert_medicamento_desconto_gestante

    def test_retorna_medicamento_desconto_aposentado(self):
        med = MedicamentoClass()
        assert_medicamento_desconto_aposentado = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip']
        assert med.sistema.medicamento_desconto_aposentado() == ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip']

    def test_retorna_medicamento_farmacia_popular(self):
        med = MedicamentoClass()
        assert_medicamento_farmacia_popular = ['doril', 'buscopan', 'paracetamol']
        assert med.sistema.medicamento_farmacia_popular() == assert_medicamento_farmacia_popular

    def test_retorna_medicamento_quantidade_comprimidos(self):
        assert_quantidade_comprimidos = 120
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip']
        med = MedicamentoClass()
        assert med.sistema.medicamento_quantidade_comprimidos(lista_de_compras) == assert_quantidade_comprimidos

    def test_retorna_medicamento_quantidade_comprimidos_nao_genericos(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip']
        assert_quantidade_comprimidos = 70
        med = MedicamentoClass()
        assert med.sistema.medicamento_quantidade_comprimidos_nao_genericos(lista_de_compras) == assert_quantidade_comprimidos

    def test_retorna_medicamento_quantidade_comprimidos_genericos_com_desconto_para_aposentados(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_quantidade_comprimidos = 50
        med = MedicamentoClass()
        assert med.sistema.medicamento_quantidade_comprimidos_genericos_com_desconto_para_aposentados(lista_de_compras) == assert_quantidade_comprimidos

    def test_retorna_medicamento_quantidade_comprimidos_genericos_com_desconto_para_gestantes(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_quantidade_comprimidos = 30
        med = MedicamentoClass()
        assert med.sistema.medicamento_quantidade_comprimidos_genericos_com_desconto_para_gestantes(lista_de_compras) == assert_quantidade_comprimidos

    def test_retorna_medicamento_quantidade_comprimidos_nao_genericos_com_desconto_para_aposentados(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_quantidade_comprimidos = 70
        med = MedicamentoClass()
        assert med.sistema.medicamento_quantidade_comprimidos_nao_genericos_com_desconto_para_aposentados(lista_de_compras) == assert_quantidade_comprimidos

    def test_retorna_medicamento_quantidade_comprimidos_nao_genericos_com_desconto_para_gestantes(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_quantidade_comprimidos = 70
        med = MedicamentoClass()
        assert med.sistema.medicamento_quantidade_comprimidos_nao_genericos_com_desconto_para_gestantes(lista_de_compras) == assert_quantidade_comprimidos

    def test_retorna_medicamento_preco_lista_de_compras(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip']
        assert_preco_medicamentos = 31.5
        med = MedicamentoClass()
        assert med.sistema.medicamento_preco_lista_de_compras(lista_de_compras) == assert_preco_medicamentos

    def test_retorna_medicamento_preco_nao_genericos(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip']
        assert_preco = 16.5
        med = MedicamentoClass()
        assert med.sistema.medicamento_preco_nao_genericos(lista_de_compras) == assert_preco

    def test_retorna_medicamento_preco_genericos_com_desconto_para_aposentados(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_preco = 15.0
        med = MedicamentoClass()
        assert med.sistema.medicamento_preco_genericos_com_desconto_para_aposentados(lista_de_compras) == assert_preco

    def test_retorna_medicamento_preco_genericos_com_desconto_para_gestantes(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_preco = 8.5
        med = MedicamentoClass()
        assert med.sistema.medicamento_preco_genericos_com_desconto_para_gestantes(lista_de_compras) == assert_preco

    def test_retorna_medicamento_preco_nao_genericos_com_desconto_para_aposentados(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_preco = 16.5
        med = MedicamentoClass()
        assert med.sistema.medicamento_preco_nao_genericos_com_desconto_para_aposentados(lista_de_compras) == assert_preco

    def test_retorna_medicamento_preco_nao_genericos_com_desconto_para_gestantes(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_preco = 16.5
        med = MedicamentoClass()
        assert med.sistema.medicamento_preco_nao_genericos_com_desconto_para_gestantes(lista_de_compras) == assert_preco
        
    def test_retorna_medicamento_quantidade_comprimidos_nao_genericos_com_farmacia_popular(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip']
        assert_quantidade_comprimidos = 40
        med = MedicamentoClass()
        assert med.sistema.medicamento_quantidade_comprimidos_nao_genericos_com_farmacia_popular(lista_de_compras) == assert_quantidade_comprimidos

    def test_retorna_medicamento_quantidade_comprimidos_genericos_com_desconto_para_aposentados_com_farmacia_popular(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_quantidade_comprimidos = 20
        med = MedicamentoClass()
        assert med.sistema.medicamento_quantidade_comprimidos_genericos_com_desconto_para_aposentados_com_farmacia_popular(lista_de_compras) == assert_quantidade_comprimidos

    def test_retorna_medicamento_quantidade_comprimidos_genericos_com_desconto_para_gestantes_com_farmacia_popular(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_quantidade_comprimidos = 20
        med = MedicamentoClass()
        assert med.sistema.medicamento_quantidade_comprimidos_genericos_com_desconto_para_gestantes_com_farmacia_popular(lista_de_compras) == assert_quantidade_comprimidos

    def test_retorna_medicamento_quantidade_comprimidos_nao_genericos_com_desconto_para_aposentados_com_farmacia_popular(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_quantidade_comprimidos = 40
        med = MedicamentoClass()
        assert med.sistema.medicamento_quantidade_comprimidos_nao_genericos_com_desconto_para_aposentados_com_farmacia_popular(lista_de_compras) == assert_quantidade_comprimidos

    def test_retorna_medicamento_quantidade_comprimidos_nao_genericos_com_desconto_para_gestantes_com_farmacia_popular(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_quantidade_comprimidos = 40
        med = MedicamentoClass()
        assert med.sistema.medicamento_quantidade_comprimidos_nao_genericos_com_desconto_para_gestantes_com_farmacia_popular(lista_de_compras) == assert_quantidade_comprimidos

    def test_retorna_medicamento_preco_lista_de_compras_com_farmacia_popular(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip']
        assert_preco_medicamentos = 13.5
        med = MedicamentoClass()
        assert med.sistema.medicamento_preco_lista_de_compras_com_farmacia_popular(lista_de_compras) == assert_preco_medicamentos

    def test_retorna_medicamento_preco_nao_genericos_com_farmacia_popular(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip']
        assert_preco = 9.0
        med = MedicamentoClass()
        assert med.sistema.medicamento_preco_nao_genericos_com_farmacia_popular(lista_de_compras) == assert_preco

    def test_retorna_medicamento_preco_genericos_com_desconto_para_aposentados_com_farmacia_popular(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_preco = 4.5
        med = MedicamentoClass()
        assert med.sistema.medicamento_preco_genericos_com_desconto_para_aposentados_com_farmacia_popular(lista_de_compras) == assert_preco

    def test_retorna_medicamento_preco_genericos_com_desconto_para_gestantes_com_farmacia_popular(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_preco = 4.5
        med = MedicamentoClass()
        assert med.sistema.medicamento_preco_genericos_com_desconto_para_gestantes_com_farmacia_popular(lista_de_compras) == assert_preco

    def test_retorna_medicamento_preco_nao_genericos_com_desconto_para_aposentados_com_farmacia_popular(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_preco = 9.0
        med = MedicamentoClass()
        assert med.sistema.medicamento_preco_nao_genericos_com_desconto_para_aposentados_com_farmacia_popular(lista_de_compras) == assert_preco

    def test_retorna_medicamento_preco_nao_genericos_com_desconto_para_gestantes_com_farmacia_popular(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_preco = 9.0
        med = MedicamentoClass()
        assert med.sistema.medicamento_preco_nao_genericos_com_desconto_para_gestantes_com_farmacia_popular(lista_de_compras) == assert_preco
      
    def test_retorna_medicamento_quantidade_comprimidos_nao_genericos_sem_farmacia_popular(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip']
        assert_quantidade_comprimidos = 30
        med = MedicamentoClass()
        assert med.sistema.medicamento_quantidade_comprimidos_nao_genericos_sem_farmacia_popular(lista_de_compras) == assert_quantidade_comprimidos

    def test_retorna_medicamento_quantidade_comprimidos_genericos_com_desconto_para_aposentados_sem_farmacia_popular(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_quantidade_comprimidos = 30
        med = MedicamentoClass()
        assert med.sistema.medicamento_quantidade_comprimidos_genericos_com_desconto_para_aposentados_sem_farmacia_popular(lista_de_compras) == assert_quantidade_comprimidos

    def test_retorna_medicamento_quantidade_comprimidos_genericos_com_desconto_para_gestantes_sem_farmacia_popular(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_quantidade_comprimidos = 10
        med = MedicamentoClass()
        assert med.sistema.medicamento_quantidade_comprimidos_genericos_com_desconto_para_gestantes_sem_farmacia_popular(lista_de_compras) == assert_quantidade_comprimidos

    def test_retorna_medicamento_quantidade_comprimidos_nao_genericos_com_desconto_para_aposentados_sem_farmacia_popular(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_quantidade_comprimidos = 30
        med = MedicamentoClass()
        assert med.sistema.medicamento_quantidade_comprimidos_nao_genericos_com_desconto_para_aposentados_sem_farmacia_popular(lista_de_compras) == assert_quantidade_comprimidos

    def test_retorna_medicamento_quantidade_comprimidos_nao_genericos_com_desconto_para_gestantes_sem_farmacia_popular(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_quantidade_comprimidos = 30
        med = MedicamentoClass()
        assert med.sistema.medicamento_quantidade_comprimidos_nao_genericos_com_desconto_para_gestantes_sem_farmacia_popular(lista_de_compras) == assert_quantidade_comprimidos

    def test_retorna_medicamento_preco_lista_de_compras_sem_farmacia_popular(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip']
        assert_preco_medicamentos = 18.0
        med = MedicamentoClass()
        assert med.sistema.medicamento_preco_lista_de_compras_sem_farmacia_popular(lista_de_compras) == assert_preco_medicamentos

    def test_retorna_medicamento_preco_nao_genericos_sem_farmacia_popular(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip']
        assert_preco = 7.5
        med = MedicamentoClass()
        assert med.sistema.medicamento_preco_nao_genericos_sem_farmacia_popular(lista_de_compras) == assert_preco

    def test_retorna_medicamento_preco_genericos_com_desconto_para_aposentados_sem_farmacia_popular(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_preco = 10.5
        med = MedicamentoClass()
        assert med.sistema.medicamento_preco_genericos_com_desconto_para_aposentados_sem_farmacia_popular(lista_de_compras) == assert_preco

    def test_retorna_medicamento_preco_genericos_com_desconto_para_gestantes_sem_farmacia_popular(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_preco = 4.0
        med = MedicamentoClass()
        assert med.sistema.medicamento_preco_genericos_com_desconto_para_gestantes_sem_farmacia_popular(lista_de_compras) == assert_preco

    def test_retorna_medicamento_preco_nao_genericos_com_desconto_para_aposentados_sem_farmacia_popular(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_preco = 7.5
        med = MedicamentoClass()
        assert med.sistema.medicamento_preco_nao_genericos_com_desconto_para_aposentados_sem_farmacia_popular(lista_de_compras) == assert_preco

    def test_retorna_medicamento_preco_nao_genericos_com_desconto_para_gestantes_sem_farmacia_popular(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_preco = 7.5
        med = MedicamentoClass()
        assert med.sistema.medicamento_preco_nao_genericos_com_desconto_para_gestantes_sem_farmacia_popular(lista_de_compras) == assert_preco

    def test_retorna_medicamento_preco_genericos_com_desconto_para_gestantes_com_desconto_aposentado_com_farmacia_popular(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_preco = 4.5
        med = MedicamentoClass()
        assert med.sistema.medicamento_preco_genericos_com_desconto_para_gestantes_com_desconto_aposentado_com_farmacia_popular(lista_de_compras) == assert_preco

    def test_retorna_medicamento_preco_nao_genericos_sem_desconto_para_gestantes_sem_desconto_aposentado_sem_farmacia_popular(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_preco = 3.0
        med = MedicamentoClass()
        assert med.sistema.medicamento_preco_nao_genericos_sem_desconto_para_gestantes_sem_desconto_aposentado_sem_farmacia_popular(lista_de_compras) == assert_preco

    def test_retorna_medicamento_preco_nao_genericos_sem_desconto_para_gestantes_sem_desconto_aposentado_sem_farmacia_popular_quantidade_miligramas_200mg(self):
        lista_de_compras = ['doril', 'resfenol', 'benegrip', 'buscopan', 'paracetamol', 'multigrip', 'neosaldina']
        assert_preco = 3.0
        med = MedicamentoClass()
        assert med.sistema.medicamento_preco_nao_genericos_sem_desconto_para_gestantes_sem_desconto_aposentado_sem_farmacia_popular_quantidade_miligramas_200mg(lista_de_compras) == assert_preco

