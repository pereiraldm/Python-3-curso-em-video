pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = pt
cont = 1
t = 0
m = 10
while m != 0:
    t = t + m
    while cont <= t:
        print(f'{termo} ->', end='')
        termo += r
        cont += 1
    print(' PAUSA')
    m = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')
print(f'Progressão finalizada com {t} termos mostrados')
