'''
Enunciado:

Faça um mini-sistema que utilize o interactive help
do Python. O usuário vai digitar o comando e o manual
vai aparecer. Quando o usuário digitar a palavra
'FIM' o programa se encerrará.

OBS: USE CORES.

#Sozinho
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

'''
#Com GB Incrivel como ele consegue fazer parecer tão simples Kkkkkk

from time import sleep
c = ['\033[m', # 0 Sem cores
     '\033[0;30;41m', # 1 vermelho
     '\033[0;30;42m', # 2 verde
     '\033[0;30;45m', # 3 amarelo
     '\033[0;30;45m', # 4 azul
     '\033[0;30;45m', # 5 roxo
     '\033[7;37m' # 6 branco
     ]

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(1)

def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print(c[cor], end='')
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)
    print(c[0], end='')
    sleep(1)


#Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA Pyhelp', 2)
    comando = str(input('Função ou biblioteca: ')).strip()
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
