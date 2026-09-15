def leiaDinheiro(msg):
    valido = False
    while not valido:
        valor = str(input(msg)).strip().replace(',', '.')
        if valor.isalpha() or valor == '':
            print(f'\033[0;31mERRO: "{valor}" é um valor inválido!\033[m')
        else:
            valido = True
            return float(valor)

# A seguir é uma redundância, pois a função leiaDinheiro já faz a validação de entrada de dados. No entanto, a função leiaFloat foi mantida para fins de compatibilidade com o código existente.
def leiaFloat(msg):
    while True:
        valor = input(msg).strip().replace(',', '.')
        if valor.isalpha() or valor == '':
            print(f'\033[0;31mERRO: "{valor}" é um valor inválido!\033[m')
        else:
            return float(valor)
        