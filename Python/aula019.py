pessoas = {'nome': 'Lucas', 'sexo': 'M', 'idade': 22}
pessoas['peso'] = 78
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
for k, v in pessoas.items():
    print(f'{k} = {v}')
print(pessoas.values())
print(pessoas.items())
print(pessoas.keys())

brasil1 = []
estado1 = {'uf': 'São Paulo', 'sigla': 'SP'}
estado2 = {'uf': 'Paraná', 'sigla': 'PR'}
brasil1.append(estado1)
brasil1.append(estado2)
print(brasil1[1]['sigla'])
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
