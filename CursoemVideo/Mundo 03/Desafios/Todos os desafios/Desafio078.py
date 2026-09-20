'''lista = list()
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
print('=-'*40)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado é {max(lista)} encontrado nas posições ', end='')
for pos, conteudo in enumerate(lista):
    if conteudo == max(lista):
        print(f'{pos}', end='... ')
print(f'\nO menor valor digitado é {min(lista)} encontrado nas posições ', end='')
for pos, conteudo in enumerate(lista):
    if conteudo == min(lista):
        print(f'{pos}', end='... ')'''
#Com GB
listanum = list()
maior = 0
menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = listanum[c]
        menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print('=-'*40)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')

