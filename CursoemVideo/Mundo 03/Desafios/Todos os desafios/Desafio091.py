'''
Crie um programa onde 4 jogadores joguem um dado
e trenham resultados aleatórios. Guarde esses
resultados num dicionário. No final, coloque esse
dicionário em ordem, sabendo que o vencedor
tirou o maior número no dado.

#SOZINHO

from random import randint
from time import sleep
dicionario = dict()

num = 1
for c in range(1, 5):
    dicionario[f'jogador {c}'] = randint(1, 6)
    print(f'O jogador {c} tirou {dicionario[f'jogador {c}']}')
    sleep(0.8)
print('Ranking dos jogadores:')
ranking = sorted(dicionario.items(), key = lambda item: item[1], reverse = True)

for k, v in ranking:
    print(f'{num}° lugar: {k} com {v}')
    num += 1
    sleep(0.8)
'''
#COM GB
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6),
        }
ranking = {} #para colocar em ordem é necessário criar um novo dicionário
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.8)
print('-='*30)
ranking = sorted(jogo.items(), key= itemgetter(1), reverse = True)
#O item getter vai pegar o item (x) do dicionário e ordená - lo.
print(ranking) # O resultado sai como uma lista e não como um dicionário. Por isso devo tratá-lo como uma lista
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(0.8)
