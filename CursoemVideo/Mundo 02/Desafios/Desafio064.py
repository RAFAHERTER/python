num = 0
contador = 0
soma = 0
while num != 999:
    num = int(input('Digite a quantidade de números que quiser: '))
    contador += 1
    if num != 999:
        soma += num
print('Você digitou {} números'.format(contador))
print('E a soma entre eles é {}'.format(soma))
print('Fim do programa!')