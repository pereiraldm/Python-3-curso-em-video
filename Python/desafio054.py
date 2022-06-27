import datetime
t1 = 0
t2 = 0
for c in range(0, 7):
    a = int(input('Qual o ano do seu nascimento? '))
    if datetime.date.today().year - a >= 21:
        t1 += 1
    else:
        t2 += 1
print(f'{t1} pessoas são maiores de idade e {t2} são menores de idade')


