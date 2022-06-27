import random
a = str(input('Digite o nome do 1: '))
b = str(input('Digite o nome do 2: '))
c = str(input('Digite o nome do 3: '))
d = str(input('Digite o nome do 4: '))
lista = [a, b, c, d]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi o {escolhido}')
