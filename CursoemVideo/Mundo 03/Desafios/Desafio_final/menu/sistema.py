import sys
import os
from number.numeros import leiaInt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def opcoes():
    print('-'*50)
    print('MENU PRINCIPAL'.center(50))
    print('-'*50)
    print("""1 -- Ver pessoas cadastradas
2 -- Cadastrar nova pessoa
3 -- Sair do Sistema
    """)
    print('='*50)
    escolha = leiaInt('Sua opção: ')
    return escolha

