print('  CONTROLE DE TERRA  ')
print('-'*40)


def area(a, b):
    s = a*b
    print(f'A área de um terreno {a}mX{b}m é de {s}m²')


largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)

