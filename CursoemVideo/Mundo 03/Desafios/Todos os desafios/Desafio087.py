"""
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados

B) A soma dos valores da terceira coluna

C) O maior valor da segunda linha

#SOZINHO

lista = [ [] , [], [] ]
soma_par = 0
for c in range(0, 3):
    for p in range(0, 3):
        num = int(input(f'Digite um valor para [{c}, {p}] : '))
        lista[c].append(num)
        if num % 2 == 0:
            soma_par += num
print('-='*30)
maior_valor = 0
soma_3coluna = 0
for c in lista:
    for pos, p in enumerate(c):
        print(f'[  {p:2}  ]', end=' ')
    soma_3coluna += c[2]
    print()
print('-='*30)
print(f'A soma de todos os números pares é {soma_par}')
print(f'A soma dos valores da terceira coluna é {soma_3coluna}')
print(f'O maior valor da segunda coluna é {max(lista[1])}')
"""
#COM GB
matriz = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]
spar = maior = soma_col = 0
for l in range(0, 3): #LINHA
    for c in range(0, 3): #COLUNA
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-='*30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    soma_col += matriz[l][2] # [LINHA] [COLUNA]
print(f'A soma dos valores da terceira coluna é {soma_col}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')

