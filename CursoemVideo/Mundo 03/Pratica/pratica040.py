from random import randint
lista = list()
par = maior = posicao = 0


for c in range(1, 11):
    lista.append(randint(0,101))
lista_tupla = tuple(lista)
print(lista_tupla)

for pos, c in enumerate(lista_tupla):
    if c % 2 == 0:
        par += 1
    if pos == 0:
        maior = c
        posicao = pos
    if c > maior:
        maior = c
        posicao = pos


print(f'Na lista gerada aleatoriamente tem {par} números pares')
print(f'O maior valor é {max(lista_tupla)} e está na posição {lista_tupla.index(max(lista_tupla)) + 1}') #Posso usar a maneira da 'RAÇA' para chegar no resultado também com a variável 'posicao' que eu criei.
print(f'Os números em ordem descrescente são:\n'
      f'{sorted(lista_tupla , reverse=True)}')
