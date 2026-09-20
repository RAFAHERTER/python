'''
Faça um programa que tenha uma função chamada 'contador()'
que receba três parâmetros: início, fim e passo e realize
a contagem.

Seu programa tem que realizar 3 contagens através da função
criada:

a) De 1 até 10, de 1 em 1.

b) De 10 até 0, de 2 em 2.

c) Uma contagem personalizada.

#SOZINHO
from time import sleep
def contador(i, f, p):
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    print('-='*30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if f < i :
        p *= -1
        for c in range(i, f-1, p):
            print(c, end=' ')
            sleep(0.4)
    elif f > i:
        for c in range(i, f+1, p):
            print(c, end=' ')
            sleep(0.4)
    else:
        print('Sequência IMPOSSÍVEL, pois o INÍCIO é igual ao FIM')
    print('FIM!')
    print('-=' * 30)
    sleep(0.8)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
contador(int(input('Início: ')),
         int(input('Fim: ')),
         int(input('Passo: ')))
'''
#COM GB
from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end=' ')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end=' ')
            sleep(0.5)
            cont -= p
        print('FIM!')

#Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)
