from random import randint
import time
from operator import itemgetter
dados = {'jogador1' : randint(1, 6),
         'jogadro2' : randint(1, 6),
         'jogador3' : randint(1, 6),
         'jogador4' : randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for j, k in dados.items():
    print(f'    O {j} tirou {k}')
    time.sleep(1)
print('-='*30)
print('Ranking dos jogadores:')
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    time.sleep(1)
