"""
Tratamento de erros 

Erros e Exceções

print(x)  # NameError: nome 'x' não está definida, ou seja, não existe.

#Isso é uma exceção e não um erro.


n = int(input('número: '))
print(f'Você digitou o número {n}') #Value error: se o usuário digitar uma letra, por exemplo, o programa vai quebrar. 


a = int(input('Numerador: '))
b = int(input('Denominador: '))
r = a / b #Zero division error: se o usuário digitar 0, o programa vai quebrar. Na matemática não existe uma divisão feita por 0.
print(f'O resultado é {r}')

r = 2 / '2'  #TypeError: não é possível dividir um número por uma string.
print(f'O resultado é {r}')


lst = [3,6,4]
print(lst[3])  # IndexError: list index out of range

import uteis #Se não existir o módulo uteis, o programa vai quebrar. 
ModuleNotFoundError: No module named 'uteis'

Keyerror: 'nome'  #Se não existir a chave 'nome' no dicionário, o programa vai quebrar.

ConnectionError: Se não houver conexão com a internet, o programa vai quebrar.

RuntimeError: Erro de tempo de execução, ou seja, o programa vai quebrar durante a execução.

E0FError: Se o usuário apertar Ctrl + D, o programa vai quebrar.

#

Vamos aprender a mexer com o comando try, except, else e finally para tratar os erros e exceções.

try:
    print(x)  # NameError: nome 'x' não está definida, ou seja, não existe.
except NameError:
    print('Variável x não definida.')

#

"""
try: #Posso ter vários tipos de except dentro de um try, mas não é uma boa prática. Pois o usuário pode não entender e se sentir confuso.

    #Posso mostrar que tipo de erro foi, mas não é uma boa prática mostrar o tipo de erro para o usuário final. Pois ele pode não entender e se sentir confuso. Além disso , pode ser perigoso mostrar o tipo de erro, pois o usuário pode tentar explorar a falha do sistema.

    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except (ValueError, TypeError):
    print(f'Tivemos um problema com os tipos de dados que você digitou')

except ZeroDivisionError:
    print(f'Não é possível dividir um número por zero.')

except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')

else:
    print(f'O resultado é {r}')

finally:
    print('Volte sempre! Muito obrigado!')