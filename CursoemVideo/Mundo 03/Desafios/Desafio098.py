'''
Faça um programa que tenha uma função chamada 'contador()'
que receba três parâmetros: início, fim e passo e realize
a contagem.

Seu programa tem que realizar 3 contagens através da função
criada:

a) De 1 até 10, de 1 em 1.

b) De 10 até 0, de 2 em 2.

c) Uma contagem personalizada.

'''
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
    sleep(0.8)


contador(1, 10, 1)
contador(10, 0, 2)
contador(int(input('Início: ')),
         int(input('Fim: ')),
         int(input('Passo: ')))


