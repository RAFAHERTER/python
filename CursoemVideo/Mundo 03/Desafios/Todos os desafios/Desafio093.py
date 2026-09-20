'''
enunciado:
Crie um programa que gerencie o aproveitamento de
um jogador de futebol. O programa vai ler o nome
do jogador e quantas partidas ele jogou.
No final, tudo isso será guardado num dicionário,
incluindo o total de gols feito durante o campeonato

#SOZINHO

dicionario= dict()
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

'''
#COM GB
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total']= sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'   =>Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
