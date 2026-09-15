'''
Enunciado:

Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a 
possibilidade da digitação de um número tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

'''
def leiaInt(msg):
    valor = input(msg).strip()
    while True:
        try:
            return int(valor)
            
        
        except:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            valor = input(msg).strip()


def leiaFloat(msg):
    valor = input(msg).replace(',', '.').strip()
    while True:
        try:
            return float(valor)
            
        except:
            print('\033[0;31mERRO! Digite um número real válido.\033[m')
            valor = input(msg).replace(',', '.').strip()

num1 = leiaInt('Digite um número inteiro: ')
num2 = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o número {num1}')
print(f'Você acabou de digitar o número {num2}')
