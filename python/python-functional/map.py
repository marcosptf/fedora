#
#map() - function
#

#o mapeamento consiste em aplicar uma function a todos so itens de uma sequencia, gerando outra sequencia
#contendo os resultados e com o mesmo tamenho da sequancia inicial;

#exemplo
nums = range(1, 11)
from math import log10
print(list(map(log10, nums)))
print(list(map(lambda x: x / 3, nums)))

#python debugger
>>> nums = range(1, 11)
>>> from math import log10
>>> print(list(map(log10, nums)))
[0.0, 0.3010299956639812, 0.47712125471966244, 0.6020599913279624, 0.6989700043360189, 0.7781512503836436, 0.8450980400142568, 0.9030899869919435, 0.9542425094393249, 1.0]
>>> 
>>> print(list(map(lambda x: x / 3, nums)))
[0.3333333333333333, 0.6666666666666666, 1.0, 1.3333333333333333, 1.6666666666666667, 2.0, 2.3333333333333335, 2.6666666666666665, 3.0, 3.3333333333333335]
>>> 
>>> 

