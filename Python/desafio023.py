n = int(input('Digite um número inteiro entre 0 a 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(n)
print(f'Primeiro número: {u}')
print(f'Segundo número: {d}')
print(f'Terceiro número: {c}')
print(f'Quarto número: {m}')
