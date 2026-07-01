'''num = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
num3= num // num2
resto = num % num2
print('O resultado da divisão inteira entre {} e {} é igual a {} e resta {}'.format(num,num2,num3, resto))'''

valor= int(input('Digite um número: '))
print('Unidades: {}'.format(valor%10))
print('Dezenas: {}'.format(valor//10 % 10))
print('Centenas: {}'.format(valor//100 % 10))
print('Milhares: {}'.format(valor//1000 % 10))
print('Dezenas de Milhares: {}'.format(valor//10000 % 10))
print('Centenas de Milhares: {}'.format(valor//100000 % 10))


