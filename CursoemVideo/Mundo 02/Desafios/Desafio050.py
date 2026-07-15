s = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        s = s + num
        cont = cont + 1
print('Você informou {} número pares, e a soma é igual a {}'.format(cont, s))
