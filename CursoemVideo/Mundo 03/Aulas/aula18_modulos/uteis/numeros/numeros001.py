def fatorial(numero):
    f = 1
    for c in range(1, numero + 1):
        f *= c
    return f

def leiaInt(msg):
    while True:
        valor = input(msg)
        if valor.isnumeric():
            break
        else:
            print('ERRO!! Digite apenas números inteiros: ')
    return int(valor)

def dobro(numero):
    return numero * 2

def triplo(numero):
    return numero*3 
