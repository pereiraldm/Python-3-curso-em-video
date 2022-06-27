def aumentar(num=0, a=0, formato=False):
    res = num + num * (a/100)
    return res if formato is False else moeda(res)


def diminuir(num=0, a=0, formato=False):
    res = num - num*(a/100)
    return res if formato is False else moeda(res)


def metade(num=0, formato=False):
    res = num / 2
    return res if formato is False else moeda(res)


def dobro(num=0, formato=False):
    res = num * 2
    return res if formato is False else moeda(res)


def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')


def resumo(num=0, taxa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(num)}')
    print(f'Dobro do preço: \t{dobro(num, True)}')
    print(f'Metade do preço: \t{metade(num, True)}')
    print(f'Com {taxa}% de aumento: {aumentar(num, taxa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(num, taxar, True)}')
    print('-' * 30)