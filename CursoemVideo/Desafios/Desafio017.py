from math import sqrt, pow
catop= float(input('Insira o valor do cateto oposto, em centímetros: '))
catadj= float(input('Insira o valor do cateto adjacente, em centímetros: '))
hip= sqrt((pow(catop,2)+ pow(catadj,2)))
print('O valor da hipotenusa para um triângulo retângulo com os lados {} e {} é igual a {}'
      .format(catop,catadj,hip))
