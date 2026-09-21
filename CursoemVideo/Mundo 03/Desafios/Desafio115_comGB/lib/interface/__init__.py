def linha(tam = 42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    resposta = leiaInt("\033[32mSua Opção: \033[m")
    return resposta

def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
        except ValueError, TypeError:
            print('\033[31mERRO!! Por favor digite um número inteiro VÁLIDO\033[m')
        except KeyboardInterrupt:
            print('O usuário preferiu responder esse valor')
            return 0
        else:
            return valor