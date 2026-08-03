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
    print(f'Jogo {c+1}: {lista}')
    lista.clear()
    sleep(1)
print('='*30)
print('BOA SORTE!'.center(30))

