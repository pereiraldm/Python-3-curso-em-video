escolha = 'S'
valores = list()
while escolha == 'S':
    num = (int(input('Digite um valor: ')))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar')
    escolha = str(input('Deseja continuar? [S/N] ')).upper().split()[0]
    while escolha not in 'SN':
        escolha = str(input('ERRO!!! Por favor, escolha entre "S" e "N". Deseja continuar? [S/N] ')).upper().split()[0]
    if escolha == 'N':
        break
print('-='*40)
valores.sort()
print(f'Você digitou os valores {valores}')
