print('-' * 40)
n = int(input('Quer ver a tabuada de qual valor? '))
print('-' * 40)
while True:
    for c in range(1, 11):
        t = c * n
        print(f'{n} x {c} = {t}')
    print('-' * 40)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40)
    if n < 0:
        break
print('PROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE!')

