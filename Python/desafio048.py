soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print(f'Existem {cont} números divisiveis por 3,', end=' ')
print(f'e a soma entre eles é de {soma}', end=' ')
