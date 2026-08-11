'''
ENUNCIADO:
Aprimore o desafio 093 para que funcione com vários jogadores,
incluindo um sistema de vizualização de detalhes do
aproveitamento de cada jogador.

#SOZINHO

lista = list()
dicionario= {}
gols = []
soma_gols = 0
while True:
    dicionario['Nome'] = input('Nome do jogador: ')
    dicionario['Jogos'] = int(input('Quantidade de jogos: '))
    for c in range(0, dicionario['Jogos']):
        num_gols = int(input(f'Quantos gols na partida {c}: '))
        gols.append(num_gols)
        soma_gols += num_gols
    dicionario['Gols'] = gols[:]
    dicionario['Total de gols'] = soma_gols
    lista.append(dicionario.copy())
    gols.clear()
    soma_gols = 0
    escolha = input('Quer continuar? [S/N] ').strip().upper()[0]
    while escolha not in 'SN':
        escolha = input('Quer continuar? [S/N] ').strip().upper()[0]
    if escolha in 'N':
        break
    print('-'*30)
print('-='*30)
print(f'{"cod":}', f'{"nome":>5}', f'{"gols":>10}', f'{"total":>10}')
print('-'*40)

for pos, c in enumerate(lista):
    print(pos , f'{c["Nome"]:>5}', f'{c["Gols"]}', f'{c["Total de gols"]:>10}')
print('-'*40)
while True:
    show_dados = int(input('Mostrar dados de qual jogador? '))
    if show_dados == 999:
        break
    elif show_dados >= len(lista):
        print(f'\033[3;31mERRO!\033[m Não existe jogador com código {show_dados}!Tente novamente.')
    elif 0 <= show_dados < len(lista):
        print(f' -- LEVANTAMENTO DO JOGADOR {lista[show_dados]["Nome"].upper()}:')
        for c in range(0, lista[show_dados]["Jogos"]):
            print(f'No jogo {c} fez {lista[show_dados]["Gols"][c]} gols.')
    print('-'*30)
print('<< VOLTE SEMPRE >>'.center(30))
'''
#COM GB
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total']= sum(partidas)
    time.append(jogador.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta in 'N':
        break
print('-='*30)
print('cod ', end='')
for i in jogador.keys(): #CABEÇALHO
    print(f'{i:<15} ', end='')
print('-' * 40)
for k, v in enumerate(time): #DADOS
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15} ', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO!! Não existe jogador com código {busca}!')
    else:
        print(f'  --- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'     No jogo {i+1} fez {g} gols.')
    print('-'*40)
print(' <<VOLTE SEMPRE>>')
