numero = int(input('Digite um número inteiro: '))
resultado = numero % 2
if resultado == 0:
    print('O número {} é par.'.format(numero))
else:
    print('O número {} é impar.'.format(numero))
