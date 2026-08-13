'''
Faça um programa que tenha uma função chamada 'maio()', que
receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer
qual deles é o maior.

#SOZINHO
from time import sleep

def maior(*valores):
    for c in valores:
        print(f'{c}', end=' ')
        sleep(0.5)
    print(f'Foram informados {len(valores)} valores ao todo')
    print(f'O maior valor informado foi {max(valores)}')
    print('-=' * 30)


print('-=' * 30)
maior(2, 9, 4, 5, 7, 1)
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior(0)
'''
#COM GB
from time import sleep
def maior(*num):
    print('-=' * 30)
    contador = maior = 0
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.3)
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1
    print(f'Foram informados {contador} valores')
    print(f'O maior valor informado foi {maior}')
#Programa Principal
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1, 2)
maior(6)
maior()
