num = int(input('Digite um número: '))
ultimo = 0
resto = 0
soma = 0
print('A soma dos dígitos', end=' ')
while num != 0:
    resto = num // 10
    ultimo = num % 10
    soma += ultimo
    num = resto
    print('{}'.format(ultimo), end=' ')
print('\né igual a {}'.format(soma))
