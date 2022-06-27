p = float(input('Insira o valor do produto: R$ '))
d = (p*0.05)
df = (p-d)
print('A valor do produto era de {:.2f}, mas com o desconto de 5% agora é {:.2f}!'.format(p, df))