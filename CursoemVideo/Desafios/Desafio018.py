import math
ang= float(input('Digite um valor de um ângulo: '))
sin = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O seno do ângulo {} é igual a {}'
      '\n O cosseno é igual a {}\n E a tangente é igual a {}'.format(ang, sin, cos, tan))