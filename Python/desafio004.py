n = input('digite algo ')

print('Só tem espaço?', n.isspace())

print('letras', n.isalpha())

print('numeros', n.isnumeric())

print('numeros ou letras', n.isalnum())

print('Está em mnúsculo?', n.isupper())

print('letras em capslock?', n.isupper())

print('esse numero vale:', format(n))
