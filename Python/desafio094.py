lista = []
dados = {}
pessoas = media = 0
while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo: [M/F] ')).upper().split()[0]
    while dados["sexo"] not in 'MF':
        dados['sexo'] = str(input('EERO!!Sexo: [M/F] ')).upper().split()[0]
    dados['idade'] = int(input('Idade: '))
    pessoas += 1
    media += dados["idade"]
    lista.append(dados.copy())
    dados.clear()
    escolha = str(input('Deseja continuar? [S/N] ')).upper().split()[0]
    while escolha not in 'SN':
        escolha = str(input('ERRO!!Deseja continuar? [S/N] ')).upper().split()[0]
    if escolha == 'N':
        break
print('-='*40)
print(f'- O grupo tem {pessoas} pessoas.')
print(f'- A média de idade é de {media/pessoas:.2f} anos')
print(f'- As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}', end=' ')
print()
print(f'- Lista das pessoas que estão acima da média: ')
for p in lista:
    if p['idade'] >= media/pessoas:
        print('           ')
        for k, v in p.items():
            print(f'{k} = {v}', end=' ')
print()
print('<< ENCERRADO >>')
