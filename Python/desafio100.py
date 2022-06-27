from random import randint

print(f'Sorteando 5 valores da lista: ')


def sorteia(lista):
    for n in range(0, 5):
        num = randint(1, 10)
        numeros.append(num)
        print(num, end=' ')
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)

