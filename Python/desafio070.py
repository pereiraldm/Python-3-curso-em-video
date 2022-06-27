escolha = 'S'
titulo = 'LOJA DO PEREIRA'
produto = 0
print('='*40)
print(titulo.center(40))
print('='*40)
total = produto1000 = preco = soma = menor = 0
barato = ' '
while escolha == 'S':
    produto = input('Nome do produto: ')
    preco = float(input('Preço: R$'))
    escolha = str(input('Deseja continuar? [S/N]')).upper().split()[0]
    total += preco
    soma += 1
    while escolha != 'S' and escolha != 'N':
        escolha = str(input('Deseja continuar? [S/N]')).upper().split()[0]
    if preco > 1000:
        produto1000 += 1
    if soma == 1 or preco < menor:
        menor = preco
        barato = produto
print(f'FIM DO PROGRAMA')
print(f'O total da comprao foi R${total}')
print(f'Temos {produto1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi o {barato} que custa R${menor}')
