lista = [  ]
dados = list()
tot = produto = estoque = total_estoque = 0
while True:
    dados.append(input('Nome do produto: '))
    produto = float(input('Qual o valor do produto: '))
    estoque = int(input('Quantidade em estoque: '))
    tot = produto * estoque
    total_estoque += tot
    dados.append(produto)
    dados.append(estoque)
    dados.append(tot)
    lista.append(dados[:])
    dados.clear()

    escolha = str(input('Quer continuar? [ S / N ] ')).strip().upper()[0]
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [ S / N ] ')).strip().upper()[0]
    if escolha in 'N':
        break
print('-='*30)

print('ESTOQUE'.center(50))
print(f'{"No":<5}', f'{"PRODUTO":<8}', f'{"VALOR (un)":>14}', f'{"QNTT EM ESTOQUE":>20}', f'{"TOTAL":>15}')
for pos, i in enumerate(lista):
    print(f'{pos + 1:<5}' f'{i[0]:<8}', f'{i[1]:>14}', f'{i[2]:>20}', f'{i[3]:>15}')
print('-=' * 30)
print(f'{"TOTAL: ":<}' f'O valor total do estoque é igual a {total_estoque:>8.2f}')

