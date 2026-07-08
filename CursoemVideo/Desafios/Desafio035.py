print('Irei te auxiliar falando sobre as condições de existência'
      'de um triângulo')
lado1 = float(input('Digite o valor do primeiro lado: '))
lado2 = float(input('Digite o valor do segundo lado: '))
lado3 = float(input('Digite o valor do terceiro lado: '))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado3 and lado2 + lado3 > lado1 :
    print('O triângulo pode ser formado.')
else:
    print('O triângulo não pode ser formado.')
