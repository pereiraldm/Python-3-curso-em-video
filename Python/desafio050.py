s = 0
for c in range(s, 6):
    n = int(input('Digite um número: '))
    p = n % 2
    if p == 0:
        s += n
print(s)
