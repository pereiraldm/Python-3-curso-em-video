escolha = 'S'
lista = list()
c = 0
while escolha == 'S':
    num = int(input('Digite um número: '))
    lista.append(num)
    c += 1
    escolha = str(input('Deseja continuar? [S/N] ')).upper().split()[0]
    if escolha == 'N':
        break
print('-='*30)
if 5 in lista:
    print('O número 5 está na lista')
else:
    print('Não há número 5 na lista')
print(f'Foram mostrados {c} números')
lista.sort(reverse=True)
print(lista)
