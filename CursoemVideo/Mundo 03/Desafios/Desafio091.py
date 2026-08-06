from random import randint
from time import sleep
dicionario = dict()

num = 1
for c in range(1, 5):
    dicionario[f'jogador {c}'] = randint(1, 6)
    print(f'O jogador {c} tirou {dicionario[f'jogador {c}']}')
    #sleep(0.5)
print('Ranking dos jogadores:')
ranking = sorted(dicionario.items(), key = lambda item: item[1], reverse = True)

for k, v in ranking:
    print(f'{num}° lugar: {k} com {v}')
    num += 1
