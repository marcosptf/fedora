#filter  - function
#
#esta funcao filter significa que uma determinada function sera aplicada em todos os itens de uma sequencia e se caso 
#a funcao retornar verdadeira, o item original fara parte da sequencia resultante
#
#exemplo:
nums = range(1, 11)
print(list(filter(lambda x : x % 2, nums)))

#a variavel nums retorna valores de 1 ~ 10
>>> for a in nums:                                                                                                                                                                                     
...     print(a)                                                                                                                                                                                       
...                                                                                                                                                                                                    
1                                                                                                                                                                                                      
2                                                                                                                                                                                                      
3
4
5
6
7
8
9
10
>>> 

#a function lambda:
#recebe um parametro, e no corpo da function verifica se o valor eh impar
lambda x : x % 2

#na function filter, tem dois parametros, 
#no primeiro ela pode receber uma function ou uma lambda
#segundo parametro recebe um valor a ser usado na funcao lambda
#a function filter, retorna o parametro nums caso na function lambda return true
filter(lambda x : x % 2, nums)

#caso o valor retorne true na function lambda, a filter retorna o valor nums e eh 
#atribuido para ser um item da list()
print(list(filter(lambda x : x % 2, nums)))

