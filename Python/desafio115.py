from funcoes import dados

def titulo(txt=''):
    print('-' * 40)
    print(txt.center(40))
    print('-' * 40)


def opcoes():
    print('\033[33m1 -\033[m \033[34mVer pessoas cadastradas\033[m\n'
          '\033[33m2 -\033[m \033[34mcadastrar nova pessoa\033[m\n'
          '\033[33m3 -\033[m \033[34msair do sistema\033[m')
    print('-' * 40)


def escolha(esc=0):
    while True:
        try:
            esc = int(input('\033[32mSua Opção: \033[m'))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite uma dessas opções ->\033[m \033[33m1 / 2 / 3.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não escolher uma opção número.\033[m.')
            return titulo(txt='Saindo do sistema... até logo!')
        else:
            if esc == 1:
                titulo(txt='Opção 1')
            elif esc == 2:
                titulo(txt='Opção 2')
            elif esc == 3:
                titulo(txt='Saindo do sistema... até logo!')
                break
            elif esc != 3 or 2 or 1:
                print('\033[31mNúmero invalido, esolha entre ->\033[m \033[33m1 / 2 / 3.\033[m')
                continue




titulo(txt='MENU PRINCIPAL')
opcoes()
escolha()
