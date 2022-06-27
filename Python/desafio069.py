maisde18 = h = mulher20 = 0
escolha = 'S'
while escolha != 'N':
    print('-' * 40)
    print('CADASTRE UMA PESSOA')
    print('-' * 40)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().split()[0]
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo: [M/F] ')).upper().split()[0]
    escolha = str(input('Deseja continuar? [S/N] ')).upper().split()[0]
    while escolha != 'S' and escolha != 'N':
        escolha = str(input('Deseja continuar? [S/N] ')).upper().split()[0]
    if idade > 18:
        maisde18 += 1
    if sexo == 'M':
        h += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    if escolha == 'N':
        break
print('='*10, 'FIM DO PROGRAMA', '='*10)
print(f'Total de pessoas com mais de 18 anos: {maisde18}')
print(f'Ao todo temos {h} homens cadastrados')
print(f'E temos {mulher20} mulheres com menos de 20 anos')
