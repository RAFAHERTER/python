"""
Modularização = Ato de construir módulos

Sistemas cada vez maiores.
Porém existe programas que exigem vários outros arquivos

Foco: Dividir um programa grande em partes
Aumentar a legibilidade.

Programas com muitas linhas, tendem a ficar difíceis de
enxergar onde possa fazer possíveis alterações.

Facilita a manutenção do programa.


"""
#TEORIA + PRÁTICA

def fatorial(numero):
    f = 1
    for c in range(1, numero + 1):
        f *= c
    return f

num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')

