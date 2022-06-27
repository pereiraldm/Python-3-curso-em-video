lista = ['macarrão', 'sorvete', 'chocolate']
print(lista)
lista.append('Suco')
print(lista)
lista.insert(2,'Cachorro-quente')
print(lista)
lista.remove('macarrão')
lista.pop()
del lista[1]
print(lista)

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valro {v}!')
print('Cheguei ao final da lista.')

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'lista B: {b}')
