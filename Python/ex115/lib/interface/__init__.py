from ex115.lib.arquivo import *


arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criararquivo(arq)


def titulo(txt):
    print('-' * 40)
    print(txt.center(40))
    print('-' * 40)


def opcoes(lista):
    c = 1
    print('-' * 40)
    for item in lista:
        print(f'\033[33m{c} -\033[m \033[34m{item}\033[m')
        c += 1
    print('-' * 40)


def leiaInt(n):
    while True:
        try:
            n = int(input(n))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m.')
            return 0
        else:
            return n



def escolha(esc=0):
    while True:
        try:
            opcoes(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
            esc = int(input('\033[32mSua Opção: \033[m'))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite uma dessas opções ->\033[m \033[33m1 / 2 / 3.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não escolher uma opção número.\033[m.')
            return titulo('Saindo do sistema... até logo!')
        else:
            if esc == 1:
                titulo('Opção 1')
                lerarquivo(arq)
            elif esc == 2:
                titulo('Novo cadastro')
                nome = str(input('Nome: '))
                idade = leiaInt('Idade: ')
                cadastrar(arq, nome, idade)
            elif esc == 3:
                titulo('Saindo do sistema... até logo!')
                break
            elif esc != 3 or 2 or 1:
                print('\033[31mNúmero invalido, esolha entre ->\033[m \033[33m1 / 2 / 3.\033[m')
                continue
