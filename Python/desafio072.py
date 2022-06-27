contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
x = 'S'
while True:
    escolha = int(input('Digite um número entre 0 e 20: '))
    while escolha < 0 or escolha > 20:
        escolha = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    for c in contagem:
        print(f'Você digitou o número {contagem[escolha]}')
        break
    x = str(input('Deseja continuar? [S/N] ')).upper().split()[0]
    if x == 'N':
        break
print('FIM DO PROGRAMA')
