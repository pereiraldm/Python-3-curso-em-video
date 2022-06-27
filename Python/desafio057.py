sexo = str(input('Digite o sexo [ M ]  [ F ]: ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
#while sexo not in 'MF':
    sexo = str(input(('\033[1;031mERRO, POR FAVOR DIGITE M OU F\033[m'
                      ' \nDigite o sexo [ M ]  [ F ]:\033[m ')).strip().upper())[0]

print('OK')
