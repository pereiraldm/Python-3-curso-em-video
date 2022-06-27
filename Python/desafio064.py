n = int(input('Digite um número inteiro: '))
soma = n
c = 0
while n != 999:
    n = int(input('Digite um número inteiro: '))
    if n != 999:
        soma += n
    c += 1
print()
print(f'Os valores digitados foram {c} e a soma deles é {soma}')
