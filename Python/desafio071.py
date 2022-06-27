titulo = 'BANCO PEREIRA'
print('='*40)
print(titulo.center(40))
print('='*40)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
cont = 0
while True:
    if total >= ced:
        total -= ced
        cont += 1
    else:
        if cont > 0:
            print(f'Total de {cont} cédular de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        cont = 0
        if total ==0:
            break
print('='*40)
print('VOLTE SEMPRE AO BANCO PEREIRA')
