from time import sleep


def maior(*num):
    tam = len(num)
    print('-='*30)
    print('Analisando os valores passados...')
    for pos in num:
        sleep(0.5)
        print(pos, end=' ')
    sleep(0.5)
    if tam == 0:
        print('A sua sequencia não possui números')
        print(f'foram informados 0 valores ao todo.')
    else:
        print(f'foram informados {tam} valores ao todo.')
        print(f'O maior valor informado foi {max(num)}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
