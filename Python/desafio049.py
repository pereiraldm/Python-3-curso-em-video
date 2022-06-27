n = int(input('Digite um valor: '))
print('-' * 12)
print(f'A tabuada do {n} é:')
for c in range(1, 11):
      t = c * n
      print (f'{n}x{c} = {t}')
print('-' * 12)