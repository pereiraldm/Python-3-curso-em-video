n = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print(f'Os valor digitados foram {n}')
if 3 in n:
    print(f'O número 3 apareceu na {n.index(3) +1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'O valor 9 apareceu {n.count(9)} vezes')
print('Os valores pares digitados foram:', end=' ')
for p in n:
    if p % 2 == 0:
        print(p, end=' ')