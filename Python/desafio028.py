import random
import time
x = random.randint(0, 5)
print('-=-'*20)
print('O programa vai pensar em um número de 0 a 5, tente adivinhar!')
print('-=-'*20)
n = int(input('Qual número o programa pensou? '))
print('Analisando...')
time.sleep(2)
if n == x:
    print(f'Parabéns você ganhou, o número sortiado foi {x}')
else:
    print(f'Você perdeu, o número sortiado foi {x},boa sorte na próxima!')