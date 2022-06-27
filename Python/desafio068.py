import random
frase = 'VAMOS JOGAR PAR OU ÍMPAR'
print('-='*20)
print(frase.center(40))
print('-='*20)
cont = par = impar = 0
while True:
    jogador = int(input('Escolha um número: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).upper().split()[0]
    print('-'*40)
    x = random.randint(0, 10)
    soma = jogador + x
    p = soma % 2
    print(f'Você jogou {jogador} e o computador {x}. total de {soma}', end=' - ')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    if escolha == 'P':
        if soma % 2 == 0:
            print('-' * 40)
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    elif escolha == 'I':
        if soma % 2 == 1:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print('-=' * 20)
print(f'GAME OVER! Você veceu {cont} vezes')
