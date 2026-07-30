dados = (5, 2, 8, 2, 9, 5, 1, 8, 3, 9)
lista = list()
for c in dados:
    if c not in lista:
        lista.append(c)
    
print(lista)

