pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = pt
cont = 1
while cont <= 10:
    print(f'{termo} ->', end='')
    termo += r
    cont += 1
print(' FIM')
print(f'\nA razão dessa PA é {r}')
print(f'O primeiro termo dessa PA é {pt}')