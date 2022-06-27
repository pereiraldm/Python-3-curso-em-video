valores = [[], []]
for c in range(0, 7):
    num = int(input(f'Digite o {c+1}º valor: '))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
print(f'A ordem crescente dos pares é: {sorted(valores[0])}')
print(f'A ordem crescente dos impares é: {sorted(valores[1])}')
