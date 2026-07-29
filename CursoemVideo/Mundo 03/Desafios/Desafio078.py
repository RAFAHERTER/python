lista = list()
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
        print(f'{pos}', end='... ')

