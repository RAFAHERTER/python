lar=float(input('Qual a largura da parede, em metros? '))
alt=float(input('Qual a altura da parede, em metros? '))
print('A área da parede é {}m² e\n'
      'a quantidade de tinta necessária para '
      'pintar\n essa parede, em litros, é {}. '
      .format((lar*alt), (lar*alt)/2))
