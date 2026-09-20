'''
Enunciado:

Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a 
possibilidade da digitação de um número tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

'''
def leiaInt(msg):
    try:
        valor = input(msg).strip()
    except KeyboardInterrupt:
        print('O usuário preferiu não digitar esse número')
        return 0
    while True:
        try:
            return int(valor)

        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse número')
            return 0
        except:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')

            try:
                valor = input(msg).strip()
            except KeyboardInterrupt:
                print('O usuário preferiu não digitar esse número')
                return 0
        

       
def leiaFloat(msg):
    try:
        valor = input(msg).replace(',', '.').strip()
    except KeyboardInterrupt:
        print('O usuário preferiu não digitar esse número')
        return 0

    while True:
        try:
            return float(valor)
            
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse número')
            return 0
        except:
            print('\033[0;31mERRO! Digite um número real válido.\033[m')

            try:
                valor = input(msg).replace(',', '.').strip()

            except KeyboardInterrupt:
                print('O usuário preferiu não digitar esse número')
                return 0


num1 = leiaInt('Digite um número inteiro: ')
num2 = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o número {num1}')
print(f'Você acabou de digitar o número {num2}')
