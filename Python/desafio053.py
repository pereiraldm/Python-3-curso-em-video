frase = str(input('Digite uma frase: ')).strip().lower()
p = frase.split()
j = ''.join(p)
i = ''
for letra in range(len(j) -1, -1, -1):
    i += j[letra]
print(j, i)
if i == j:
    print('É palíndromo')
else:
    print('Não é palíndromo')