from ..number.numeros import leiaInt


def opcoes():
    print("""1 -- Ver pessoas cadastradas
2 -- Cadastrar nova pessoa
3 -- Sair do Sistema
    """)
    print('='*50)
    escolha = leiaInt('Sua opção: ')
    return escolha

def painel(msg):
    print('-'*50)
    print(f'{msg}'.center(50))
    print('-'*50)
