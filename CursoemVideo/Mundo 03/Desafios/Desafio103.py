def ficha(nome = '', gols = 0):
    if nome == '':
        nome = '<desconhecido>'
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


#Programa principal
jogador = str(input('Nome do jogador: ')).strip()
qtt = int(input('Quantidade de gols: '))
if qtt > 0:
    ficha(jogador, qtt)
elif qtt == '':
    ficha(jogador, 0)


