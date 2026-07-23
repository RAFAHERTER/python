'''num = input('Digite um número inteiro: ')
invertido = num[::-1]
print(invertido)
'''

#Agora matemáticamente
num = int(input('Digite um número inteiro: '))
resto = 0
ultimo = 0
invertido = 0
if num == 0:
    print('Não existe o inverso de 0')
elif num != 0:
    print('O inverso de {} é igual a '.format(num), end='')
    while num != 0:
        resto = num // 10
        ultimo = num % 10
        num = resto
        invertido = invertido * 10 + ultimo
    print(invertido)
