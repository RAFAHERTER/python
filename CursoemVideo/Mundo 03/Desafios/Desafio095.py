dicionario= {}
dicionario['Nome'] = input('Nome do jogador: ')
dicionario['Jogos'] = int(input('Quantidade de jogos: '))
gols = []
soma_gols = 0
for c in range(0, dicionario['Jogos']):
    num_gols = int(input(f'Quantos gols na partida {c}: '))
    gols.append(num_gols)
    soma_gols += num_gols
dicionario['Gols'] = gols[:]
dicionario['Total de gols'] = soma_gols
print('-='*30)
print(dicionario)
print('-=' *30)
for k, v in dicionario.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {dicionario['Nome']} jogou {dicionario["Jogos"]} partidas.')
for c in range(0, dicionario['Jogos']):
    print(f'{"=>":>4} Na partida {c}, fez {dicionario["Gols"][c]} gols.')
print(f'Foi um total de {soma_gols} gols.')

