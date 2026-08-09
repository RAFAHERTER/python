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

