v = float(input('Qual o valor da casa? R$'))
s = float(input('Qual o salário do comprador? R$'))
a = int(input('Em quantos anos ele vai pagar? '))
m = a * 12
p = v / m
print(f'Você pagará em \033[33m{m}\033[m meses')
print(f'Seu salário é de \033[34mR${s:.2f}\033[m, e 30% dele é \033[36mR${s*0.3:.2f}\033[m')
print(f'As parcelas mensais serão de \033[35mR${p:.2f}\033[m')
if p > (s*0.3):
    print('\033[30;41mInfelizmente a compra da casa não será permitida.\033[m')
else:
    print('\033[30;42mParabéns você está prestes a comprar sua casa!\033[m')
