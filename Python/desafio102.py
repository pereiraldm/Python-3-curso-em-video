def fatorial(n, show=False):
    '''
    -> Calcula o fatorial de um numero.
    :param n: O npumero a ser calculado.
    :param show: (opicional) mostrar ou nao a conta.
    :return: o valor do fatorial de um numero.
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f



n = int(input('Digite um número: '))
print(fatorial(n, show=True))
