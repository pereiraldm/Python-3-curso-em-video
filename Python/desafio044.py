print('{:=^40}'.format(' LOJA DO PEREIRA '))
p = float(input('Digite o preço da compra: R$'))
print('''Escolha a sua forma de pagamento:
[ 1 ] dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão ''')
f = int(input('Escolha a forma de pagamento: '))
if f == 1:
    print('R$', p - (p*0.10))
elif f == 2:
    print('R$', p - (p*0.05))
elif f == 3:
    print(f'R${p}')
elif f == 4:
    print('R$', p + (p*0.20))

