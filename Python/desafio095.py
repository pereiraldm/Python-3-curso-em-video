time = list()
dados = {}
lista = []
while True:
    dados.clear()
    dados['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    lista.clear()
    for g in range(0, partidas):
        lista.append(int(input(f'Quantos gols na partida {g+1}? ')))
    dados['gols'] = lista[:]
    dados['total'] = sum(lista)
    time.append(dados.copy())
    escolha = str(input('Deseja continuar? [S/N] ')).upper().split()[0]
    while escolha not in 'SN':
        escolha = str(input('ERRO!!Deseja continuar? [S/N] ')).upper().split()[0]
    if escolha == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15} ', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'     No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('<< VOLTE SEMPRE >>')
