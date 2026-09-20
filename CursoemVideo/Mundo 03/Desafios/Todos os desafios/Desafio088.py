'''
Faça um programa que ajude um jogador
da MEGA SENA a criar palpites. O programa
vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60
para cada jogo, cadastrando tudo em uma
lista composta.

#SOZINHO

from random import randint
from time import sleep
lista = list()
print('='*30)
print('MEGA SENA!!'.center(30))
print('='*30)
jogo = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'SORTEANDO {jogo} JOGOS'.center(30))
for c in range(0,jogo):
    for d in range(0,6):
        aleatorio = randint(1, 60)
        lista.append(aleatorio)
        lista.sort()
    print(f'Jogo {c+1}: {lista}')
    lista.clear()
    sleep(1)
print('='*30)
print('BOA SORTE!'.center(30))
'''
#COM GB
from random import randint
from time import sleep
lista = list()
jogos = list()
print('-'*30)
print('JOGA NA MEGA SENA'.center(30))
print('-'*30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3, f'SORTEANDO {quant} JOGOS', '-='*3)
for i, c in enumerate(jogos):
    print(f'Jogo {i+1}: {c}')
    sleep(1)
print('-='*5, '< BOA SORTE! >', '-='*5)

