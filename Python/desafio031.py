d = float(input('Digite a distância da viagme em km: '))
if d <= 200:
    p = d*0.50
else:
    p = d*0.45
print(f'O valor da sua passagem será de R${p:.2f}')