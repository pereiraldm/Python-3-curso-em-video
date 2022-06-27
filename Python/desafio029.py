v = float(input('Digite a velocidade do carro: '))
m = (v-80)*7
if v > 80:
    print(f'Você foi multado! o limite da pista é de 80km/h e sua velocidade foi de {v}km/h, sendo assim o valor da sua multa será de R${m}!')
else:
    print('Você está dentro do limite de velocidade, continue assim!')