escolha = 'S'
galera = []
medidas = []
maio = men = 0
while True:
    galera.append(str(input('Nome: ')))
    galera.append(float(input('Peso: ')))
    if len(medidas) == 0:
        maio = men = galera[1]
    else:
        if galera[1] > maio:
            maio = galera[1]
        if galera[1] < men:
            men = galera[1]
    medidas.append(galera[:])
    galera.clear()
    escolha = str(input('Deseja continuar? [S/N] ')).upper().split()[0]
    if escolha not in 'SN':
        escolha = str(input('Erro!!Deseja continuar? [S/N] ')).upper().split()[0]
    if escolha == 'N':
        break
print(f'Ao todo, você cadastrou {len(medidas)}.')
print(f'O maior peso foi de {maio}Kg. Peso de ', end='')
for p in medidas:
    if p[1] == maio:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in medidas:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
