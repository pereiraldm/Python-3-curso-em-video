linha1 = []
linha2 = []
linha3 = []
pares = soma = 0
for c in range(0, 3):
    num = int(input(f'Digite um valor para [0, {c}]: '))
    linha1.append(num)
    if num % 2 == 0:
        pares += num
    if c == 2:
        soma += num
for c in range(0, 3):
    num = int(input(f'Digite um valor para [1, {c}]: '))
    linha2.append(num)
    if num % 2 == 0:
        pares += num
    if c == 2:
        soma += num
for c in range(0, 3):
    num = int(input(f'Digite um valor para [2, {c}]: '))
    linha3.append(num)
    if num % 2 == 0:
        pares += num
    if c == 2:
        soma += num
print('-='*40)
print(f'[ {linha1[0]} ] [ {linha1[1]} ] [ {linha1[2]} ]')
print(f'[ {linha2[0]} ] [ {linha2[1]} ] [ {linha2[2]} ]')
print(f'[ {linha3[0]} ] [ {linha3[1]} ] [ {linha3[2]} ]')
print('-='*40)
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {soma}.')
print(f'O maior valor da segunda linha é {max(linha2)}.')
