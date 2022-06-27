r = 'S'
soma = maior = menor = 0
soma2 = 0
while r == 'S':
    n = int(input('Digite um número inteiro: '))
    r = str(input('Deseja continuar? [S] [N] ')).upper().strip()[0]
    soma += n
    soma2 += 1
    if soma2 == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / soma2
print(f'A soma dos números é {soma}')
print(f'A média de {soma} é {media:.2f}')
print(f'O maior número digitado foi {maior} e o menor foi {menor}')
