lista = list()
for c in range(0, 5):
    lista.append(int(input('Digite um valor: ')))

print(f'O maior valor digitado é {max(lista)} encontrado na posição {lista.index(max(lista)) + 1}')
print(f'O menor valor digitado é {min(lista)} encontrado na posição {lista.index(min(lista)) + 1}')

