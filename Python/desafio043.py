peso = float(input('Digite seu peso em KG: '))
a = float(input('Digite sua altura em centimetros: '))
altura = a / 100
imc = peso / altura**2
print(f'{imc:.2f}')

if imc < 18.5:
    print(f'Seu IMC é de {imc:.2f}, está abaixo!')
elif 18.4 < imc < 25:
    print(f'Seu IMC é de {imc:.2f}, está no peso ideal!')
elif 24.9 < imc < 30:
    print(f'Seu IMC é de {imc:.2f}, está sobrepeso!')
elif 29.9 < imc < 40:
    print(f'Seu IMC é de {imc:.2f}, está em obresidade!')
else:
    print(f'Seu IMC é de {imc:.2f}, está em obesidade mórbida')