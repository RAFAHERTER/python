"""
Enunciado:
Faça um programa que tenha uma função chamada 'ficha()', que
receba dois parâmetros opcionais: o nome de um jogador e
quantos gols ele marcou. O programa deverá ser capaz de
mostrar a ficha do jogador, mesmo que algum dado não tenha
sido informado corretamente.

#Sozinho - Está errado... Validação de entrada não deu certo para os gols.
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
"""
#Com GB
def ficha(jog = '<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato')


#Programa Principal
n = str(input('Nome do jogador: '))
g = str(input('Quantidade de gols: '))
if g.isnumeric():
    g = int(g)
else:
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
#Solução bem eficiente

