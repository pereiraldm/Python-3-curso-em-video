from ex115.lib.interface import *
from ex115.lib.arquivo import *


arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

titulo(txt='MENU PRINCIPAL')
escolha()
