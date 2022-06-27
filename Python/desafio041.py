from datetime import date
a = int(input('Digite o ano de nascimento do atleta: '))
ano = date.today().year - a
if ano <= 9.0:
    print('MIRIM')
elif 9 < ano < 14:
    print('INFANTIL')
elif 14 < ano < 19:
    print('JUNIOR')
elif ano == 19:
    print('SÊNIOR')
elif ano >= 20:
    print('MASTER')

