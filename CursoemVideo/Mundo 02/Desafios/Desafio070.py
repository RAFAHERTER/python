print('-'*30)
print('LOJA SUPER BARATÃO'.center(30))
print('-'*30)
soma = 0
tot_prod_1000 = 0
produto_barato = ' '
preco_menor = 0
continuar = ' '
contador = 0
while True:
    nome_produto = input('Digite o nome do produto: ').strip()
    preco = float(input('Preço do produto: '))
    contador += 1
    if contador == 1:
        preco_menor = preco
        produto_barato = nome_produto
    else:
        if preco < preco_menor:
            preco_menor = preco
            produto_barato = nome_produto
    soma += preco
    continuar = input('Quer continuar? [S/N] ').strip()
    if preco > 1000:
        tot_prod_1000 += 1
    while continuar not in 'NnSs':
        continuar = input('Quer continuar? [S/N] ').strip()
    if continuar in 'Nn':
        break
print(f'O total da compra foi de R${soma:.2f}')
print(f'Temos {tot_prod_1000} produtos custando mais de R$1000')
print(f'O produto mais barato foi {produto_barato} que custa R${preco_menor:.2f}')

