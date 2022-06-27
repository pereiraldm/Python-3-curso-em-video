dados = {}
lista = []
dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for g in range(0, partidas):
    lista.append(int(input(f'Quantos gols na partida {g}? ')))
    dados['gols'] = lista[:]
    dados['total'] = sum(lista)
print('-='*30)
print(dados)
print('-='*30)
for v in dados:
    print(f'O campo {v} tem o valor {dados[v]}')
print('-='*30)
print(f'O jogador {dados["nome"]} jogou {len(dados["gols"])} partidas.')
for d, v in enumerate(dados["gols"]):
    print(f'    => Na partida {d}, fez {v} gols.')
print(f'FOi um total de {dados["total"]} gols.')
