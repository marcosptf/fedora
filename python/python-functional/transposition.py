
#transposition - function 

#transposition eh construir serie de sequencias a partir de outra serie de sequencias,
#em que a primeira nova sequencia contem o primeiro elemento de cada sequencia original,
#a segunda nova sequencia contem o segundo elemento de cada sequencia original, ate que 
#alguma das sequencias originais acabe;


#exemplo de transposition que eh implementado no python pelo interator zip();
#uma list com ('a', 1), ('b', 2) ....
from string import ascii_lowercase
print(list(zip(ascii_lowercase, range(1, 10))))

#python debugger 
>>> from string import ascii_lowercase
>>> 
>>> print(list(zip(ascii_lowercase, range(1, 10))))
[('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6), ('g', 7), ('h', 8), ('i', 9)]


#transposition de uma matriz
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list(zip(*matriz)))

#debugger python
>>> matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> print(list(zip(*matriz)))
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]

