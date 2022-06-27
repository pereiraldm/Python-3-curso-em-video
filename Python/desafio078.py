valores = list()
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {len(valores)}: ')))
print('-='*30)
for c in valores:
    print(f'O maior valor digitado foi {max(valores)} que está na posição ', end='')
    for i, v in enumerate(valores):
        if v == max(valores):
            print(f'{i}... ', end='')
    print(f'\nO menor foi número digitado foi {min(valores)} que está na posição ', end='')
    for i, v in enumerate(valores):
        if v == min(valores):
            print(f'{i}... ', end='')
    break
print(f'\nOs valores digitados foram: {valores}')
