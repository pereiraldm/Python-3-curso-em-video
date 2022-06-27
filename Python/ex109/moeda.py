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

