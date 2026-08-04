'''
Crie um programa que crie uma matriz de
dimensão 3X3 e preencha com valores lidos
pelo teclado.
No final, mostre a matriz na tela, com a
formação correta.

lista = [ [] , [], [] ]
for c in range(0, 3):
    for p in range(0, 3):
        num = int(input(f'Digite um valor para [{c}, {p}] : '))
        lista[c].append(num)
print('-='*30)
for c in lista:
    for p in c:
        print(f'[  {p:3}  ]', end=' ')
    print()
'''
#COM GB
matriz = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]
for l in range(0, 3): #LINHA
    for c in range(0, 3): #COLUNA
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()

