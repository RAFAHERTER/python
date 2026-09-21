from ..interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'r')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArq(caminho):
    try:
        a = open(caminho, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo ".txt" criado com sucesso')

def lerArquivo(caminho):
    try:
        a = open(caminho, 'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        print(a.read())