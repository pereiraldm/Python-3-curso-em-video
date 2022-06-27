soma = soma2 = 0
while True:
    n = int(input('Digite um número inteiro (999 para parar): '))
    if n != 999:
        soma += n
        soma2 += 1
    else:
        break
media = soma / soma2
print(f'{soma2} números foram digitados, a soma deles é {soma} e a média entre eles é {media:.2f}')

