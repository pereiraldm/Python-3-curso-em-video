n = int(input('Digite um número: '))
t = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        t += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end='')
print(f'\n\033[mO número {n} foi divisível {t} vezes')
if t == 2:
    print('então é primo')
else:
    print('então não é primo')

