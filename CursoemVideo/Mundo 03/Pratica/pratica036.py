from random import randint
matriz = [ [], [], [] ]

for l in range(0, 3):
    for c in range(0, 3):
        aleatorio = randint(1, 9)
        matriz[l].append(aleatorio)
        
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()