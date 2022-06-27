n1 = float(input('Digite o tamanho de uma reta: '))
n2 = float(input('Digite o tamanho de mais uma reta: '))
n3 = float(input('Digite o tamanho da última reta: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('As retas podem formar um triangulo ', end='')
    if n1 == n2 == n3:
        print('EQUILATERO!')
    elif n1 != n2 != n3 != n1:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print('As retas não podem fomrar um triangulo!')
