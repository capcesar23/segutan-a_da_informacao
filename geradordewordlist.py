import itertools

string = input('String a ser permutada: ')

resultado = itertools.permutations(string, len(string))# quantidade de caracteres e tamanho da string

for i in resultado:
    print(''.join(i))