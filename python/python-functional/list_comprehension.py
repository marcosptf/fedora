#
#list comprehension
#
#em computacao, list comprehension eh uma contrucao que equivale uma notacao matematica;
#list comprehension eh mais eficiente do que usar as funcoes map() e filter()
#tanto em termos de uso de processador quanto com consumo de memoria

#sintaxe:
lista = [<expression> for <reference> in <sequence> if <condition>]

#example
nums = range(12)

#eleve os pares ao quadrados
print([x**2 for x in nums if x % 2])

#python debugger
>>> nums = range(12)
>>> print([x**2 for x in nums if x % 2])
[1, 9, 25, 49, 81, 121]

