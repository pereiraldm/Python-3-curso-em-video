from time import sleep


def contador(a, b, c):
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    print('-='*20)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if a < b:
        while a <= b:
            print(a, end=' ')
            sleep(0.5)
            a += c
    elif a > b:
        while a >= b:
            if a < b:
                break
            sleep(0.5)
            print(a, end=' ')
            a -= c
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
