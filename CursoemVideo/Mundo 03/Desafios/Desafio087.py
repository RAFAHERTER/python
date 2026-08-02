"""
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados

B) A soma dos valores da terceira coluna

C) O maior valor da segunda linha

"""
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

