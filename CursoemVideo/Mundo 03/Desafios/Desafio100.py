'''
Enunciado:
Faça um programa que tenha uma lista chamada 'números'
e duas funções chamadas 'sorteie()' e 'somaPar()'. A primeira
função vai sortear 5 números e vai colocá-los dentro da lista.
E a segunda função vai mostrar a soma entre todos os valores
pares sorteados pela função anterior.
'''
from random import randint
from time import sleep

def sorteie(lista):
    print(f'Sorteando 5 valores da lista: ', end=' ')
    for c in range(0, 5):
        lista.append(randint(0, 10))
    for i in lista:
        print(f'{i}', end=' ')
        sleep(0.3)
    print()


def soma_Par(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {aleatorio}, temos {soma} ', end=' ')


aleatorio = list()
sorteie(aleatorio)
soma_Par(aleatorio)

