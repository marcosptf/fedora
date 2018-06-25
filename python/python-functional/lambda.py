#
#lambda - funcoes anonimas
#
#syntaxe
#lambda <lista de variaveis> : <expressoes>
#
#exemplos
amp = lambda x, y, z: (x ** 2 + y ** 2 + z ** 2) ** .5

#amp se torna o nome da function
#o nome lambda indica o inicio da function
#apos o nome lambda, as variaveis sao os parametros desta function
#apos o operaror ":" existe um return implicito com todo o corpo da function
amp = lambda x, y, z: (x ** 2 + y ** 2 + z ** 2) ** .5

print(amp(1, 1, 1))
print("\n")
print(amp(3, 4, 5))

