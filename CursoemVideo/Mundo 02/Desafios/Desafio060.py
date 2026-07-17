'''from math import factorial
from time import sleep
num = int(input('Insira um número: '))
fatorial = factorial(num)
print('Calculando...')
sleep(2)
print('O fatorial de {} é {}.'.format(num, fatorial))

from math import factorial
num = 0
for c in range(1, 5):
    num = int(input('Digite um valor: '))
    fatorial = factorial(num)
    print('{}! = {}'.format(num, fatorial))
'''
from math import factorial
num = 1
while num != 0:
    num = int(input('Insira um número: '))
    if num < 0:
        print('Opção invalida! Tente novamente.')
        continue #O 'Continue pula o resto do código e o reinicia. O break interrompe e encerra o loop instantaneamente.
    fatorial = factorial(num)
    if num != 0:
        print('{}! é  {}'.format(num, fatorial))
print('Fim do programa')
