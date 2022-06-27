maior = 0
media = 0
nomevelho = ''
m20 = 0
for pessoas in range(1, 5):
    print(f'PESSOA NÚMERO {pessoas}:')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input(' [ M ]   [ F ]: ')).strip()
    media += idade
    if pessoas == 1 and sexo in 'Mm':
        maior = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maior:
        maior = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        m20 += 1

m = media / 4
print(f'A média das idades é: {m}.')
print(f'O homem mais velho tem {maior} e se chama {nomevelho}.')
print(f'Há {m20} mulheres com menos de 20 anos.')

