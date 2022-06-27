from random import sample
print('-'*30)
print(f'      JOGA NA MEGA SENA       ')
print('-'*30)
qnt = int(input('Quantos jogos você quer que eu sorteie? '))
nums = [sample(range(1, 61), k=6) for x in range(0, qnt)]
for c in range(0, qnt):
    print(f'Jogo {c+1}: {sorted(nums)[c]}')
