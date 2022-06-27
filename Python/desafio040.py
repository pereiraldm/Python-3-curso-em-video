n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m >= 7.0:
    print('\033[32mAPROVADO\033[m')
elif 4.9 < m <= 6.9:
    print('\033[33mRECUPERAÇÃO\033[m')
else:
    print('\033[31mREPROVADO\033[m')

