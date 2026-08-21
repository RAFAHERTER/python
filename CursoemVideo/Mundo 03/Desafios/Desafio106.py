'''
Enunciado:

Faça um mini-sistema que utilize o interactive help
do Python. O usuário vai digitar o comando e o manual
vai aparecer. Quando o usuário digitar a palavra
'FIM' o programa se encerrará.

OBS: USE CORES.
'''
from time import sleep
def interativo(comm):
    if comm == 'FIM':
        print('\033[0;41m~'*13)
        print('  ATÉ LOGO!')
        print('~'*13)
        print('\033[m')
        return comm
    else:
        print('\033[44m~'*30)
        print(f'Acessando o manual do {comm}'.center(30))
        print('~' * 30)
        sleep(1)
        print('\033[m\033[7;37;40m')
        help(comm)
        print('\033[m')

comando = ''
while comando != 'FIM':
    print('\033[0;43m-' * 30)
    print('\033[0;43mSISTEMA DE AJUDA PYTHON'.center(30))
    print('\033[0;43m-' * 30)
    comando = input('\033[mDigite um comando: ').strip()
    resp = interativo(comando)
