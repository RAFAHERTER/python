from datetime import date
atual = date.today().year
print("""Olá, tudo bem??
Vou identificar se você pode ou se tem que servir às forças armadas. 
PRESSIONE:
[ 1 ] para caso você seja HOMEM.
[ 2 ] para caso você seja MULHER""")
opcao = int(input('Sua opção: '))
if opcao == 1:
    ano = int(input('Qual ano você nasceu? '))
    idade = atual - ano
    if idade < 18:
        diferenca = 18 - idade
        alistamento = 2026 + diferenca
        print("""Você ainda vai se apresentar ao exército.
    Restam {} anos para o seu alistamento militar
    Seu alistamento militar será em {}"""
    .format(diferenca, alistamento))
    elif idade == 18:
        print('Está na hora de se alistar.')
    else:
        diferenca = idade - 18
        alistamento = 2026 - diferenca
        print("""Já passou da hora de se alistar.
Se passaram {} anos do alistamento militar
Seu alistamento militar foi em {}"""
              .format(diferenca, alistamento))
        resposta = input('Você já se alistou? ').strip().upper()
        if resposta == 'SIM':
            print('\033[34mExcelente!!\033[m')
            serviu = input('E você serviu?? ').strip().upper()
            if serviu == 'SIM':
                print('\033[34mLEGAL!!\033[m')
                tempo = int(input('Por quantos anos? '))
                if tempo == 1:
                    print('É... ano de recruta é foda mesmo kkkkkkk se fodeo.')
                elif 1 < tempo < 3 :
                    print('É... é um tempo razoável para se servir no quartel. EXCELENTE!')
                elif tempo > 3:
                    print('Caramba {} ANOS servindo?? ta maluco kkkkkk Corajoso.'.format(tempo))
                elif tempo == 0:
                    print('UÉ, TU FALOU QUE SERVIU PORRA.')
                elif tempo < 0:
                    print("""Ta de sacanagem comigo né?
    NÃO EXISTE TEMPO NEGATIVO!!
    VOLTOU NO TEMPO AGORA É??""")
                else:
                    print('\033[1;31mERRO!!\033[m')
            elif serviu == 'NAO' or serviu == 'NÃO':
                print('\033[34mSORTE SUA HAHAHA\033[m \n'
                      'O inferno não é vermelho e quente \n'
                      '\033[32mELE É VERDE E FRIO MWAHAHAHAHA\033[m')
            else:
                print('\033[34mERRO!!\033[m')
        elif resposta == 'NAO' or resposta == 'NÃO':
            print('\033[31m-\033[m'*10, '\033[31mCUIDADO!!\033[m','\033[31m-\033[m'*10)
            print('Você NÃO poderá emitir a sua reservista assim, \n'
                  'além disso será considerado como \033[1;31mDESERTOR\033[m')
        else:
            print('\033[31m-\033[m'*10, '\033[31mERRO!!\033[m','\033[31m-\033[m'*10)
elif opcao == 2:
    print("""Você não tem obrigação de fazer o alistamento militar,
porém você tem a opção de ter o serviço militar voluntário feminino.
De acordo com as novas legislações brasileiras.
    """)
else:
    print('Opção inválida TENTE NOVAMENTE')
