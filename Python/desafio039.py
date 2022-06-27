from datetime import date
d = int(input('Digite o ano do seu nascimento: '))
a = date.today().year
if a - d > 18:
    print(f'Você deve se alistar com 18 anos, você tem {a - d} anos, então já passou da data!')
elif a - d < 18:
    print(f'Você irá se alistar daqui {18 - (a - d)} ano(s)!')
else:
    print(f'Você tem {a - d} anos, está na hora de se alistar!')