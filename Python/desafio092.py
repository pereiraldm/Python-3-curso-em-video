import datetime
dados = dict()
while True:
    dados['nome'] = str(input('Nome: '))
    ano = int(input('Ano de Nascimento: '))
    dados['idade'] = datetime.date.today().year - ano
    dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
    if dados["ctps"] == 0:
        break
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = (dados["contratacao"] + 35) - ano
    break
print('-='*40)
for v in dados:
    print(f'{v} tem o valor {dados[v]}')
