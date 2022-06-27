n = float(input('Digite o valor de quantos reais tem na sua carteira R$ '))
d = float(n/3.27)
print('Com o dolar a R$3.27 e você tendo R${:.2f} na carteira, você consiguirá comprar US${:.2f} em dolares'.format(n, d))