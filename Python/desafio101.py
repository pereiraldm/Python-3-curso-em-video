import datetime



def voto(ano=0):
    if 18 <= idade <= 65:
       print('VOTO OBRIGATÓRIO.')
    elif idade < 16:
        print('VOTO NEGADO.')
    else:
        print('VOTO OPICIONAL.')


ano = int(input('Em que ano você nasceu? '))
idade = datetime.date.today().year - ano
print(f'Com {idade} anos: ', end='')
voto()
