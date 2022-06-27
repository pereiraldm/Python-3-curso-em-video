dados = dict()
lista = list()
dados['Nome'] = str(input('Nome: '))
dados['Média'] = float(input('Média: '))
dados['Situação'] = []
lista.append(dados.copy())
for n, m, s in lista:
    print('-='*30)
    print(f'{n} é igual a {dados["Nome"]}'
          f'\n{m} é igual a {dados["Média"]}')
    if dados['Média'] >= 7:
        dados['Situação'] = 'Aprovado'
        lista.append(dados.copy())
    else:
        dados['Situação'] = 'Reprovado'
        lista.append(dados.copy())
    print(f'{s} é igual a {dados["Situação"]}')
    break
