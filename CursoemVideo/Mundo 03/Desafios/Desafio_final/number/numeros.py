def leiaInt(msg):
    try:
        valor = input(msg).strip()
    except KeyboardInterrupt:
        print('O usuário preferiu não digitar um número.')
        return 0
    while True:
        try:
            return int(valor)
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar um número.')
            return 0
        except :
            print('\033[0;31mERRO!! Número inválido. Tente novamente!\033[m')
            try:
                valor = input(msg).strip()
            except KeyboardInterrupt:
                print('O usuário preferiu não digitar um número.')
                return 0

def leiaString(msg):
    while True:
        try:
            nome = input(msg).strip().title()
            nome_lista = nome.split()
            nome_acesso = nome.replace(' ', '')
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar o nome!')
            break

        if nome_acesso.isalpha():
            return nome_lista
        else:
            print(f'"{nome}" não é um nome válido! Tente novamente!')


   


