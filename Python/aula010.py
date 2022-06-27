n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua mpedia foi {m:.1f}')
if m >= 6.0:
    print('Sua nota foi boa!')
else:
    print('Sua nota foi ruim!')