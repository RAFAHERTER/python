#import math #BIBLIOTECA
#num=int(input('Digite um número: '))
#raiz= math.sqrt(num)
#print('A raiz quadrada de {} é igual a {:.2f}'
#      .format(num, math.ceil(raiz)))

from math import sqrt, ceil, floor
num=int(input('Digite um número: '))
raiz= sqrt(num)
print('A raiz de {} é igual a {:.2f}'
      .format(num, raiz))
