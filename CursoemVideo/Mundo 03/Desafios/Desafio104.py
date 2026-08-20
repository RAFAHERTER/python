def leiaInt(msg):
    global n
    num = False
    while num is False:
        n = input(msg)
        num = n.isnumeric()
        if num is False:
            print('ERRO, Digite apenas um número inteiro')
        else:
            return n

n = leiaInt('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n}')

