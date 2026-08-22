'''
ENUNCIADO:
Crie um programa que tenha função' leiaint() ', que vai funcionar
de forma semelhante à função 'input()' do python, só que
fazendo a validação para aceitar apenas um valor numérico.
Exemplo:
n = leiaint('Digite um número inteiro: ')

#Sozinho
def leiaInt(msg):
    global n
    num = False
    while num is False:
        n = input(msg)
        num = n.isnumeric()
        if num is False:
            print('\033[31mERRO, Digite apenas um número inteiro\033[m')
        else:
            return n

n = leiaInt('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n}')
'''
#Com GB
def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mERRO! Digite um número inteiro válido\033[m')
        if ok:
            break
    return valor

#Programa Principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

