from math import factorial
opçaõ = 'S'
while opçaõ == 'S':
    n = int(input('Digite um número inteiro qualquer para descobrir seu fatorial: '))
    f = factorial(n)
    print(f'O fatorial de \033[1;31m{n}\033[m é: \033[1;033m{f}\033[m')
    opçaõ = str(input('Deseja continuar? [S/N] ')).upper()
print('\033[1;107;41mVOCÊ SAIU DO PROGRAMA\033[m')



