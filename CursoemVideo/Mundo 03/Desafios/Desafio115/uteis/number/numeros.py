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
            