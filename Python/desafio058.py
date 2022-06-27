import random
import time
x = random.randint(0, 10)
erros = 0
print('-=-'*20)
print('O programa vai pensar em um número de 0 a 10, tente adivinhar!')
print('-=-'*20)
n = int(input('Qual número o programa pensou? '))
print('Analisando...')
time.sleep(0.5)
while x != n:
    if n > x:
        print('\033[1;031mMenos... tente novamente!\033[m')
    elif n < x:
        print('\033[1;031mMais... tente novamente!\033[m')
    n = int(input('Qual número o programa pensou? '))
    print('Analisando...')
    time.sleep(0.5)
    erros += 1
print(f'Parabéns, você acertou! o número pessado foi \033[1;032m{x}\033[m e para isso você percisou de \033[1;031m{erros}\033[m tentativas')
