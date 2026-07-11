print('Irei te auxiliar na denominação dos '
      'triângulos')
lado1 = float(input('Digite o valor do primeiro lado: '))
lado2 = float(input('Digite o valor do segundo lado: '))
lado3 = float(input('Digite o valor do terceiro lado: '))
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print('O triângulo pode ser formado.')
    if lado1 == lado2 and lado1 == lado3:
        print('Este triângulo é equilátero.')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Este triângulo é isósceles.')
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print('Esse triângulo é escaleno.')
else:
    print('O triângulo não pode ser formado.')
