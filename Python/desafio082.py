valores = list()
pares = list()
impares = list()
escolha = 'S'
while escolha == 'S':
    num = int(input('Digite um número: '))
    valores.append(num)
    escolha = str(input('Deseja continuar? [S/N] ')).upper().split()[0]
    if num % 2 == 0:
        pares.append(num)
    elif num % 2 == 1:
        impares.append(num)
    if escolha == 'N':
        break
print('-='*30)
print(f'Os valores digitados foram {valores}')
print(f'Os pares em {valores} são {pares}')
print(f'Os impares em {valores} são {impares}')
