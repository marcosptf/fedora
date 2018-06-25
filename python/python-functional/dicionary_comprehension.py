#
#dicionary comprehension
#
#eh uma expression que gera um dicionario como saida com uma estrutura similar ao list comprehension

#exemplo
alf = { chr(a + 65 ) : a for a in range(26) }
print(sorted(alf.keys()))

#python debugger
>>> alf = { chr(a + 65 ) : a for a in range(26) }
>>> print(sorted(alf.keys()))
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']



