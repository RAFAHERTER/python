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
    fatorial = factorial(num)
    print('{}! é  {}'.format(num, fatorial))
print('Fim do programa')
