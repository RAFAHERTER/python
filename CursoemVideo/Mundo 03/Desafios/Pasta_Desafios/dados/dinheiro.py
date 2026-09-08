def leiaDinheiro(msg):
    while True:
        valor = input(msg).strip()
        if valor.isalpha() or valor == '':
            print(f'\033[0;31mERRO: "{valor}" é um valor inválido!\033[m')
        else:
            return float(valor)

def leiaFloat(msg):
    while True:
        valor = input(msg).strip()
        if valor.isalpha() or valor == '':
            print(f'\033[0;31mERRO: "{valor}" é um valor inválido!\033[m')
        else:
            return float(valor)
        