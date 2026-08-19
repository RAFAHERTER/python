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

