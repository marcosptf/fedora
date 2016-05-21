# -*- coding: utf-8 -*-

idade = int(raw_input("coloque a sua idade: "))
mensagem_menor = "voce eh menor, ainda nao pode dirigir"
mensagem_maior = "voce eh maior, ja pode dirigir"
mensagem = mensagem_maior

if idade <= 17:
  mensagem = mensagem_menor
  
print(mensagem)
