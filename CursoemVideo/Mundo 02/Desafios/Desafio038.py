print('Comparação de números inteiros')
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
if num1 > num2:
    print('O numero \033[31m{}\033[m é o maior'.format(num1))
elif num1 < num2:
    print('O número \033[31m{}\033[m é o maior'.format(num2))
else:
    print('Os dois números são \033[31mIGUAIS!')
 