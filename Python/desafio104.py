def leiaInt(n):
    while True:
        n = str(input(n))
        if n.isnumeric():
            print(f'Você acabou de digitar o número {n}')
            break
        else:
            print('ERRO! DIgite um número inteiro válido.')







n = leiaInt('Digite um número: ')

