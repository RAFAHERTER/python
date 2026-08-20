'''
Enunciado:

Faça um mini-sistema que utilize o interactive help
do Python. O usuário vai digitar o comando e o manual
vai aparecer. Quando o usuário digitar a palavra
'FIM' o programa se encerrará.

OBS: USE CORES.
'''
def interativo():
    global resp
    while resp not in 'FIM':
        resp = input('Digite uma função: ').strip().upper()


print('\033[0;43m-'*30)
print('\033[0;43mSISTEMA DE AJUDA PYTHON'.center(30))
print('\033[0;43m-'*30)
resp = str(input(f'Função: {interativo()}'))