from lib.interface import *
from lib.arquivo import *
from time import sleep
import os


arq = "cursoemvideo.txt"
caminho_atual = os.path.dirname(__file__)
caminho_arquivotxt = os.path.join(caminho_atual, arq)
print(caminho_atual)

if not arquivoExiste(caminho_arquivotxt):
    criarArq(caminho_arquivotxt)


while True:
    resposta = menu(['Ver pessoas cadastradas', 
      'Cadastrar novas pessoas', 
      'Sair do programa'] )
    if resposta == 1 :
        lerArquivo(caminho_arquivotxt)

    elif resposta == 2:
        cabecalho('Opção 2')

    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO!! Digite uma opção válida\033[m')
    sleep(2)