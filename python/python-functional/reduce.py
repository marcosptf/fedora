#
#reduce - function
#reducao significa aplicar uma function que recebe dois parametros nos dois primeiros 
#elementos de uma lista de uma sequencia, aplicar novamente a function usando como 
#parametro o resultado do primeiro par e o terceiro elemento, seguindo assim ate o final da sequencia;
#o resultado final da reducao eh apenas um elemento;

from functools import reduce

nums = range(100)

#soma com reduce (pode concatenar com strings)
print(reduce(lambda x, y: x + y, nums))
4950

#soma mais simples so para numeros
print(sum(nums))
4950

#reduce explain
reduce(<function(x,y)>, <list>)
reduce (  este resultado sera somado ao proximo item da lista =>  <function((resultado da ultima soma da function), (segundo item da lista))>, <list>    )
                                    1                                               0                                          1                  [0, 1, 2, 3 ,4 ,5 ]               
reduce (  este resultado sera somado ao proximo item da lista =>  <function((resultado da ultima soma da function), (segundo item da lista))>, <list>    )
                                    3                                               1                                          2                  [0, 1, 2, 3 ,4 ,5 ]               
reduce (  este resultado sera somado ao proximo item da lista =>  <function((resultado da ultima soma da function), (segundo item da lista))>, <list>    )
                                    6                                               3                                          3                  [0, 1, 2, 3 ,4 ,5 ]               
reduce (  este resultado sera somado ao proximo item da lista =>  <function((resultado da ultima soma da function), (segundo item da lista))>, <list>    )
                                    10                                              6                                          4                  [0, 1, 2, 3 ,4 ,5 ]               
reduce (  este resultado sera somado ao proximo item da lista =>  <function((resultado da ultima soma da function), (segundo item da lista))>, <list>    )
                                    15                                              10                                         5                  [0, 1, 2, 3 ,4 ,5 ]               


1.ele aplica numa function que recebe dois parametros nos dois elementos de uma list; 
entao se ele recebe uma sequencia de:
0, 1, 2, 3, ,4 , 5;
ele recebe e envia para a function, os parametros 0, 1,;

2.e aplica o resultado desta soma, que seria 1 e soma com o proximo item da lista que seria 2 e o resultado eh 3;

3.sequencia de resultados
1, 3, 6, 10, 15, 21, 28

4. exemplos de teste de mesa:
0  + 1 = 1
1  + 2 = 3
3  + 3 = 6
6  + 4 = 10
10 + 5 = 15
15 + 6 = 21
21 + 7 = 28

#fizemos um debugger para tentar entender o que a function reduce() faz e qua
#eh o seu comportamento
>>> from functools import reduce
>>> nums = range(100)
>>> print(reduce(lambda x, y: x + y, nums))
4950
>>> print(sum(nums))
4950
>>> 
>>> 
>>> for a in range(5):
...     print(a)
... 
0
1
2
3
4
>>> nums = range(5)
>>> print(reduce(lambda x, y: x + y, nums))
10
>>> nums = range(1)
>>> print(reduce(lambda x, y: x + y, nums))
0
>>> nums = range(2)
>>> print(reduce(lambda x, y: x + y, nums))
1
>>> nums = range(3)
>>> print(reduce(lambda x, y: x + y, nums))
3
>>> 
>>> for a in range(3):
...     print(a)
... 
0
1
2
>>> 







