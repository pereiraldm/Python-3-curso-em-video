pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
d = pt + 9 * r
for c in range(pt, d + r, r):
    print(c, end=' -> ')
print(f'A razão dessa PA é {r}')
print(f'O primeiro termo dessa PA é {pt}')