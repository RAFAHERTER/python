ano = int(input('Qual ano você nasceu? '))
idade = 2026 - ano
if idade < 18:
    diferenca = 18 - idade
    print('Você ainda vai se apresentar ao exército.\n'
          'Resta {} anos para o seu alistamento militar'
          .format(diferenca))
elif idade == 18:
    print('Está na hora de se alistar.')

else:
    diferenca = idade - 18
    print('Já passou da hora de se alistar.\n'
          'Se passaram {} anos do alistamento militar'.format(diferenca))
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
                print('Ta de sacanagem comigo né? NÃO EXISTE TEMPO NEGATIVO!!\n'
                      'VOLTOU NO TEMPO AGORA É??')
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