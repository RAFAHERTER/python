from math import trunc
num=float(input('Digite um número real: '))
inteira=trunc(num) #Podemops utilizar o int(num) também.
print('A número {} tem por sua parte inteira '
      'igual a {:.0f}'.format(num,inteira))
