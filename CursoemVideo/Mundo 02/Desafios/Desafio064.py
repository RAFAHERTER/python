'''
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
'''
#Com GB
contador = soma = 0 #De acordo com GB 'num == 0' é uma gambiarra.
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    contador += 1
    soma += num
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} número e a soma foi {}'.format(contador, soma))

