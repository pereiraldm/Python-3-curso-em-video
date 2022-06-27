s = float(input('Digite o seu salário: R$'))
if s <= 1250:
    print(f'Seu salário de \033[34mR${s:.2f}\033[m teve um aumento de \033[36m15%\033[m, '
          f'seu salário atual é de \033[32mR${(s*0.15)+s:.2f}\033[m!')
else:
    print(f'Seu salário de R${s:.2f} teve um aumento de 10%, seu salário atual é de R${(s*0.10)+s:.2f}!')