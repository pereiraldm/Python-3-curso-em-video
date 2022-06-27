#from math import pow, sqrt
#co = float(input('Coloque o valor do cateto oposto: '))
#ca = float(input('Coloque o valor do cateto adjacente: '))
#cop = pow(co, 2)
#cad = pow(ca,2 )
#print(f'hipotenusa = {sqrt(cop+cad):.2f}')

import math
co = float(input('Coloque o valor do cateto oposto: '))
ca = float(input('Coloque o valor do cateto adjacente: '))
print(f'hipotenusa = {math.hypot(co, ca):.2f}')