'''
ENUNCIADO:
Crie um programa que tenha uma função fatorial() que receba
dois parâmetros: o primeiro que indique o número a calcular
e o outro chamado 'show', que será um valor lógico(opcional)
indicando se será mostrado ou não na tela o processo de cálculo
do fatorial.

#Sozinho
obs: O meu programa foi feito mais aprimorado, com o objetivo
de ler as variáveis, ao invés de trocar nos códigos.
def fatorial(numero, show=0 ):
    """
    -> Calcule o Fatorial de um número
    :param numero: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta do fatorial
    :return: O valor do Fatorial de um número 'n'
    """
    if show != 0:
        f = 1
        for c in range(numero, 0, -1):
            print(f'{c} -> ', end='')
            f *= c
        print(f)
    else:
        f= 1
        for c in range(numero, 0, -1):
            f *= c
        print(f)

#Programa principal
n = int(input('Digite um valor que deseja saber seu fatorial: '))
s = input('Deseja ver o processo? ').strip().upper()[0]
while s not in 'SN':
    s = input('Deseja ver o processo? ').strip().upper()[0]
if s == 'N':
    s = 0
elif s == 'S':
    s = True
fatorial(n, bool(s))

'''
#Com GB
def fatorial(n, show = False):
    """
        -> Calcule o Fatorial de um número
        :param n: O número a ser calculado
        :param show: (opcional) Mostrar ou não a conta do fatorial
        :return: O valor do Fatorial de um número 'n'
        """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

#Programa Principal
print(fatorial(5, show = True))


