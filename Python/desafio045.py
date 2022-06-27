from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Escolha pedra, papel ou tesoura:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura ''')
j = int(input(f'Qual sua escolha? '))
print('CARREGANDO...')
sleep(1)
print('-=' * 15)
print(f'O computador escolheu {itens[pc]}')
print(f'O você escolheu {itens[j]}')
print('-=' * 15)
if pc == 0:
    if j == 0:
        print('\033[1;33mEmpatou!\033[m')
    elif j == 1:
        print('\033[1;32mVocê ganhou!\033[m')
    elif j == 2:
        print('\033[1;31mVocê perdeu!\033[m')
    else:
        print('\033[7;97;31mPor favor escolha entre 0, 1 e 2\033[m')
elif pc == 1:
    if j == 0:
        print('\033[1;31mVocê perdeu!\033[m')
    elif j == 1:
        print('\033[1;33mEmpatou!\033[m')
    elif j == 2:
        print('\033[1;32mVocê ganhou!\033[m')
    else:
        print('\033[7;97;31mPor favor escolha entre 0, 1 e 2\033[m')
elif pc == 2:
    if j == 0:
        print('\033[1;32mVocê ganhou!\033[m')
    elif j == 1:
        print('\033[1;31mVocê perdeu!\033[m')
    elif j == 2:
        print('\033[1;33mEmpatou!\033[m')
    else:
        print('\033[7;97;31mPor favor escolha entre 0, 1 e 2\033[m')

