n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
o = int(input('Sua opção: '))
if o == 1:
    print(f'{n} convertido para BINÁRIO é igual a {bin(n)[2:]}')
elif o == 2:
    print(f'{n} convertido para OCTAL é igual a {oct(n)[2:]}')
elif o == 3:
    print(f'{n} convertido para HEXADECIMAL é igual a {hex(n)[2:]}')
else:
    print('Opção inválida, tente novamente')
