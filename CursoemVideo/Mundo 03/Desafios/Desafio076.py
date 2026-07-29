'''tupla = ('Lápis', 1.75,
         'Mochila', 350.00,
         'Borracha', 5.00,
         'Estojo', 25.00,
         'Caderno', 50.00,
         'Transferidor',7.80,
         'Livro', 95.40,
         'Canetas', 50.00)
produtos = tupla[0::2]
preco = tupla[1::2]
print('-'*40)
print('LISTAGEM DE PREÇOS'.center(40))
print('-'*40)
for c in range(len(produtos)):
    print(f'{produtos[c]:.<31}R${preco[c]:>7.2f}')
print('-'*40)
'''
#COM GB
#Obs: Meu exercício está errado!!
#O ojetivo era com tupla única, e eu fiz com 3
listagem = ('Lápis', 1.75,
         'Mochila', 350.00,
         'Borracha', 5.00,
         'Estojo', 25.00,
         'Caderno', 50.00,
         'Transferidor',7.80,
         'Livro', 95.40,
         'Canetas', 50.00)
print('-'*40)
print('LISTAGEM DE PREÇOS'.center(40))
print('-'*40)
for pos in range(len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<31}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')

