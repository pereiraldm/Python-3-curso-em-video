print('Escolha dois números inteiros para iniciar o programa')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opção = int(input(f'''Seus números escolhidos foram \033[1;031m{n1}\033[m e \033[1;031m{n2}\033[m, escolha o que quer fazer com eles:
[ 1 ] somar
[ 2 ] multiplicador
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Opção: '''))
while opção != 5:
    if opção == 1:
        print(f'\nA soma dos números entre \033[1;031m{n1}\033[m e \033[1;031m{n2}\033[m é \033[1;032m{n1 + n2}\033[m')
    elif opção == 2:
        print(f'\nA multiplicação entre \033[1;031m{n1}\033[m e \033[1;031m{n2}\033[m é \033[1;032m{n1 * n2}\033[m')
    elif opção == 3:
        if n1 > n2:
            print(f'\nentre \033[1;031m{n1}\033[m e \033[1;031m{n2}\033[m, o maior número é o \033[1;032m{n1}\033[m')
        elif n2 > n1:
            print(f'\nentre \033[1;031m{n1}\033[m e \033[1;031m{n2}\033[m, o maior número é o \033[1;032m{n2}\033[m')
        else:
            print(f'\n\033[1;031m{n1}\033[m e \033[1;031m{n2}\033[m são iguais')
    elif opção == 4:
        n1 = int(input('Digite o novo primeiro número: '))
        n2 = int(input('Digite o novo segundo número: '))
    opção = int(input(f'''
Seus números escolhidos foram \033[1;031m{n1}\033[m e \033[1;031m{n2}\033[m, escolha o que quer fazer com eles:
[ 1 ] somar
[ 2 ] multiplicador
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Opção: '''))
print('\033[1;107;41mVOCÊ SAIU DO PROGRAMA\033[m')
