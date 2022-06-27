from random import shuffle
a = str(input('Digite o nome do 1: '))
b = str(input('Digite o nome do 2: '))
c = str(input('Digite o nome do 3: '))
d = str(input('Digite o nome do 4: '))
lista = [a, b, c, d]
shuffle(lista)
print(f'A ordem escolhida para apresentação será: {lista}')