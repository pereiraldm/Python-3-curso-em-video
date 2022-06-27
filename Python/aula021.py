def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contage
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')

#help(contador)


def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


somar(5, 3, 8)
somar(3, 2)
somar(6)
somar(b=5, c=6)


def funcao(n2):
    n1 = 4
    n2 += 4
    n3 = 2
    print(f'N1 dentro vale {n1}')
    print(f'N2 dentro vale {n2}')
    print(f'N3 dentro vale {n3}')


n1 = 2
funcao(n1)
print(f'N1 fora vale {n1}')


def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'a dentro vale {c}')
    print(f'b dentro vale {b}')
    print(f'c dentro vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}')


def soma(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = soma(3, 2, 5)
r2 = soma(2, 2)
r3 = soma(6)

print(f'Os resultados foram {r1}, {r2} e {r3}')


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('DIgite um número: '))
if par(num):
    print('É par!')
else:
    print('É impar!')
