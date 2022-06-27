totmai = totmen = 0
teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
galera2 = []
dado = []
for c in range(0, 3):
    dado.append((str(input('Nome: '))))
    dado.append(int(input('Idade: ')))
    galera2.append(dado[:])
    dado.clear()
print(galera2)
for p in galera2:
    if p[1] >= 21:
       print(f'{p[0]} é maior de idade')
       totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores de idade e {totmen} menor de idade')
