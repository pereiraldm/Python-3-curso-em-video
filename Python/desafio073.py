colocação = ('','Corinthians', 'Santos', 'América', 'Bragantino', 'São paulo', 'Atlético mineiro',
             'Botafogo', 'Internacional', 'Coritiba','Avaí', 'Cuiabá', 'Athletico paranaense', 'Palmeiras',
             'Flamengo', 'Fluminense', 'Goiás', 'Ceará', 'Juventude', 'Atlético goianiese', 'Fortaleza')
for c in range(1, len(colocação)):
    print(f'{c}º {colocação[c]}')
print('-='*20)
print('Os 5 primeiros colocados são: ')

for c in range(1, 6):
    print(f'{c}º {colocação[c]}')
print('-='*20)
print('Os 4 últimos colocados são: ')

for c in range(16, len(colocação)):
    print(f'{c}º {colocação[c]}')
print('-='*20)
print('Os times em ordem alfabética fica assim: ')
print(sorted(colocação[1:len(colocação)]))
print('-='*20)
print(f'O Cuiabá se encontra na {colocação.index("Cuiabá")}ª posição')
