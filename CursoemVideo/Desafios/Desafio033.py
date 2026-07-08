print('====== DESAFIO 033 ======')

#Dúvida...
print('Vou dizer qual número é o maior')
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo: '))
num3 = float(input('Digite o terceiro: '))
if num1 > num2 > num3:
    print('O {} é o maior.'.format(num1))
if num2 > num3 > num1:
    print('O {} é o maior.'.format(num2))
if num3 > num1 > num2:
    print('O {} é o maior.'.format(num3))
