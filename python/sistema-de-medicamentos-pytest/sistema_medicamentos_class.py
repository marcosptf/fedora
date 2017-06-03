# -*- coding: utf-8 -*-

from lista_medicamentos_json import medicamento

class SistemaMedicamento:
  
    def __init__(self):
        med = medicamento()
        self.lista = med.lista_medicamentos_json()

    def medicamento_doril(self):
        return self.lista['medicamento'][0]['nome']

    def medicamento_generico(self):
        generico = []
        for medicamento in self.lista['medicamento']:
            if medicamento['generico']=="True":
                generico.append(medicamento['nome'])
        return generico

    def medicamento_desconto_gestante(self):
        gestante = []
        for medicamento in self.lista['medicamento']:
            if medicamento['desconto-gestantes'] == "True":
                gestante.append(medicamento['nome'])
        return gestante

    def medicamento_desconto_aposentado(self):
        aposentado = []
        for medicamento in self.lista['medicamento']:
            if medicamento['desconto-aposentados'] == "True":
                aposentado.append(medicamento['nome'])
        return aposentado

    def medicamento_farmacia_popular(self):
        farmacia_popular = []
        for medicamento in self.lista['medicamento']:
            if medicamento['farmacia-popular'] == "True":
                farmacia_popular.append(medicamento['nome'])
        return farmacia_popular

    def medicamento_quantidade_comprimidos(self, lista_de_compras):
        quantidade_comprimidos = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras:
                quantidade_comprimidos += medicamento['quantidade-comprimidos']
        return quantidade_comprimidos

    def medicamento_quantidade_comprimidos_nao_genericos(self, lista_de_compras):
        quantidade_comprimidos = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False":
                quantidade_comprimidos += medicamento['quantidade-comprimidos']
        return quantidade_comprimidos

    def medicamento_quantidade_comprimidos_genericos_com_desconto_para_aposentados(self, lista_de_compras):
        quantidade_comprimidos = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="True" and medicamento['desconto-aposentados']=="True":
                quantidade_comprimidos += medicamento['quantidade-comprimidos']
        return quantidade_comprimidos

    def medicamento_quantidade_comprimidos_genericos_com_desconto_para_gestantes(self, lista_de_compras):
        quantidade_comprimidos = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="True" and medicamento['desconto-gestantes']=="True":
                quantidade_comprimidos += medicamento['quantidade-comprimidos']
        return quantidade_comprimidos

    def medicamento_quantidade_comprimidos_nao_genericos_com_desconto_para_aposentados(self, lista_de_compras):
        quantidade_comprimidos = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['desconto-aposentados']=="True":
                quantidade_comprimidos += medicamento['quantidade-comprimidos']
        return quantidade_comprimidos

    def medicamento_quantidade_comprimidos_nao_genericos_com_desconto_para_gestantes(self, lista_de_compras):
        quantidade_comprimidos = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['desconto-gestantes']=="True":
                quantidade_comprimidos += medicamento['quantidade-comprimidos']
        return quantidade_comprimidos

    def medicamento_preco_lista_de_compras(self, lista_de_compras):
        preco_medicamentos = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras:
                preco_medicamentos += medicamento['preco']
        return preco_medicamentos

    def medicamento_preco_nao_genericos(self, lista_de_compras):
        preco = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False":
                preco += medicamento['preco']
        return preco

    def medicamento_preco_genericos_com_desconto_para_aposentados(self, lista_de_compras):
        preco = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="True" and medicamento['desconto-aposentados']=="True":
                preco += medicamento['preco']
        return preco

    def medicamento_preco_genericos_com_desconto_para_gestantes(self, lista_de_compras):
        preco = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="True" and medicamento['desconto-gestantes']=="True":
                preco += medicamento['preco']
        return preco

    def medicamento_preco_nao_genericos_com_desconto_para_aposentados(self, lista_de_compras):
        preco = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['desconto-aposentados']=="True":
                preco += medicamento['preco']
        return preco

    def medicamento_preco_nao_genericos_com_desconto_para_gestantes(self, lista_de_compras):
        preco = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['desconto-gestantes']=="True":
                preco += medicamento['preco']
        return preco
        
    def medicamento_quantidade_comprimidos_nao_genericos_com_farmacia_popular(self, lista_de_compras):
        quantidade_comprimidos = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['farmacia-popular'] == "True":
                quantidade_comprimidos += medicamento['quantidade-comprimidos']
        return quantidade_comprimidos

    def medicamento_quantidade_comprimidos_genericos_com_desconto_para_aposentados_com_farmacia_popular(self, lista_de_compras):
        quantidade_comprimidos = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="True" and medicamento['desconto-aposentados']=="True" and medicamento['farmacia-popular'] == "True":
                quantidade_comprimidos += medicamento['quantidade-comprimidos']
        return quantidade_comprimidos

    def medicamento_quantidade_comprimidos_genericos_com_desconto_para_gestantes_com_farmacia_popular(self, lista_de_compras):
        quantidade_comprimidos = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="True" and medicamento['desconto-gestantes']=="True" and medicamento['farmacia-popular'] == "True":
                quantidade_comprimidos += medicamento['quantidade-comprimidos']
        return quantidade_comprimidos

    def medicamento_quantidade_comprimidos_nao_genericos_com_desconto_para_aposentados_com_farmacia_popular(self, lista_de_compras):
        quantidade_comprimidos = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['desconto-aposentados']=="True" and medicamento['farmacia-popular'] == "True":
                quantidade_comprimidos += medicamento['quantidade-comprimidos']
        return quantidade_comprimidos

    def medicamento_quantidade_comprimidos_nao_genericos_com_desconto_para_gestantes_com_farmacia_popular(self, lista_de_compras):
        quantidade_comprimidos = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['desconto-gestantes']=="True" and medicamento['farmacia-popular'] == "True":
                quantidade_comprimidos += medicamento['quantidade-comprimidos']
        return quantidade_comprimidos

    def medicamento_preco_lista_de_compras_com_farmacia_popular(self, lista_de_compras):
        preco_medicamentos = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['farmacia-popular'] == "True":
                preco_medicamentos += medicamento['preco']
        return preco_medicamentos

    def medicamento_preco_nao_genericos_com_farmacia_popular(self, lista_de_compras):
        preco = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['farmacia-popular'] == "True":
                preco += medicamento['preco']
        return preco

    def medicamento_preco_genericos_com_desconto_para_aposentados_com_farmacia_popular(self, lista_de_compras):
        preco = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="True" and medicamento['desconto-aposentados']=="True" and medicamento['farmacia-popular'] == "True":
                preco += medicamento['preco']
        return preco

    def medicamento_preco_genericos_com_desconto_para_gestantes_com_farmacia_popular(self, lista_de_compras):
        preco = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="True" and medicamento['desconto-gestantes']=="True" and medicamento['farmacia-popular'] == "True":
                preco += medicamento['preco']
        return preco

    def medicamento_preco_nao_genericos_com_desconto_para_aposentados_com_farmacia_popular(self, lista_de_compras):
        preco = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['desconto-aposentados']=="True" and medicamento['farmacia-popular'] == "True":
                preco += medicamento['preco']
        return preco

    def medicamento_preco_nao_genericos_com_desconto_para_gestantes_com_farmacia_popular(self, lista_de_compras):
        preco = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['desconto-gestantes']=="True" and medicamento['farmacia-popular'] == "True":
                preco += medicamento['preco']
        return preco
      
    def medicamento_quantidade_comprimidos_nao_genericos_sem_farmacia_popular(self, lista_de_compras):
        quantidade_comprimidos = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['farmacia-popular'] == "False":
                quantidade_comprimidos += medicamento['quantidade-comprimidos']
        return quantidade_comprimidos

    def medicamento_quantidade_comprimidos_genericos_com_desconto_para_aposentados_sem_farmacia_popular(self, lista_de_compras):
        quantidade_comprimidos = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="True" and medicamento['desconto-aposentados']=="True" and medicamento['farmacia-popular'] == "False":
                quantidade_comprimidos += medicamento['quantidade-comprimidos']
        return quantidade_comprimidos

    def medicamento_quantidade_comprimidos_genericos_com_desconto_para_gestantes_sem_farmacia_popular(self, lista_de_compras):
        quantidade_comprimidos = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="True" and medicamento['desconto-gestantes']=="True" and medicamento['farmacia-popular'] == "False":
                quantidade_comprimidos += medicamento['quantidade-comprimidos']
        return quantidade_comprimidos

    def medicamento_quantidade_comprimidos_nao_genericos_com_desconto_para_aposentados_sem_farmacia_popular(self, lista_de_compras):
        quantidade_comprimidos = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['desconto-aposentados']=="True" and medicamento['farmacia-popular'] == "False":
                quantidade_comprimidos += medicamento['quantidade-comprimidos']
        return quantidade_comprimidos

    def medicamento_quantidade_comprimidos_nao_genericos_com_desconto_para_gestantes_sem_farmacia_popular(self, lista_de_compras):
        quantidade_comprimidos = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['desconto-gestantes']=="True" and medicamento['farmacia-popular'] == "False":
                quantidade_comprimidos += medicamento['quantidade-comprimidos']
        return quantidade_comprimidos

    def medicamento_preco_lista_de_compras_sem_farmacia_popular(self, lista_de_compras):
        preco_medicamentos = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['farmacia-popular'] == "False":
                preco_medicamentos += medicamento['preco']
        return preco_medicamentos

    def medicamento_preco_nao_genericos_sem_farmacia_popular(self, lista_de_compras):
        preco = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['farmacia-popular'] == "False":
                preco += medicamento['preco']
        return preco

    def medicamento_preco_genericos_com_desconto_para_aposentados_sem_farmacia_popular(self, lista_de_compras):
        preco = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="True" and medicamento['desconto-aposentados']=="True" and medicamento['farmacia-popular'] == "False":
                preco += medicamento['preco']
        return preco

    def medicamento_preco_genericos_com_desconto_para_gestantes_sem_farmacia_popular(self, lista_de_compras):
        preco = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="True" and medicamento['desconto-gestantes']=="True" and medicamento['farmacia-popular'] == "False":
                preco += medicamento['preco']
        return preco

    def medicamento_preco_nao_genericos_com_desconto_para_aposentados_sem_farmacia_popular(self, lista_de_compras):
        preco = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['desconto-aposentados']=="True" and medicamento['farmacia-popular'] == "False":
                preco += medicamento['preco']
        return preco

    def medicamento_preco_nao_genericos_com_desconto_para_gestantes_sem_farmacia_popular(self, lista_de_compras):
        preco = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['desconto-gestantes']=="True" and medicamento['farmacia-popular'] == "False":
                preco += medicamento['preco']
        return preco

    def medicamento_preco_genericos_com_desconto_para_gestantes_com_desconto_aposentado_com_farmacia_popular(self, lista_de_compras):
        preco = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="True" and medicamento['desconto-gestantes']=="True" and medicamento['desconto-aposentados']=="True"  and medicamento['farmacia-popular'] == "True":
                preco += medicamento['preco']
        return preco

    def medicamento_preco_nao_genericos_sem_desconto_para_gestantes_sem_desconto_aposentado_sem_farmacia_popular(self, lista_de_compras):
        preco = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['desconto-gestantes']=="False" and medicamento['desconto-aposentados']=="False" and medicamento['farmacia-popular'] == "False":
                preco += medicamento['preco']
        return preco

    def medicamento_preco_nao_genericos_sem_desconto_para_gestantes_sem_desconto_aposentado_sem_farmacia_popular_quantidade_miligramas_200mg(self, lista_de_compras):
        preco = 0
        for medicamento in self.lista['medicamento']:
            if medicamento['nome'] in lista_de_compras and medicamento['generico']=="False" and medicamento['desconto-gestantes']=="False" and medicamento['desconto-aposentados']=="False" and medicamento['farmacia-popular'] == "False" and medicamento['miligramas'] == "200mg":
                preco += medicamento['preco']
        return preco
