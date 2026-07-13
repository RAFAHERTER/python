print('Irei te auxiliar na denominação dos '
      'triângulos')
lado1 = float(input('Digite o valor do primeiro lado: '))
lado2 = float(input('Digite o valor do segundo lado: '))
lado3 = float(input('Digite o valor do terceiro lado: '))
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print('Os segmentos acima podem formar um triângulo ', end='')
    if lado1 == lado2 == lado3:
        print('EQUILÁTERO!')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('ISÓSCELES!')
    elif lado1 != lado2 != lado3 != lado1:
        print('ESCALENO!')
else:
    print('O triângulo não pode ser formado.')
