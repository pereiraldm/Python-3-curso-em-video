def aumentar(num=0, a=0):
    res = num + num * (a/100)
    return res


def diminuir(num=0, a=0):
    res = num - num*(a/100)
    return res


def metade(num=0):
    res = num / 2
    return res


def dobro(num=0):
    res = num * 2
    return res


def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')
