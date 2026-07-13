"""from random import choice
from time import sleep
print('Vamos jogar JOKENPÔ')
lista = ['Pedra', 'Papel', 'Tesoura']
escolha = choice(lista)
jogador = input('Escreva aqui a sua esolha: ').strip().upper()
print('JO')
sleep(0.8)
print('KEN')
sleep(0.8)
print('PÔ')
print('-='*10)
if jogador == 'PEDRA' and escolha == 'Pedra':
    print('Foi um EMPATE!! \nEu também escolhi Pedra.')
elif jogador == 'PEDRA' and escolha == 'Papel':
    print('Você PERDEUU!! \nEu escolhi Papel.')
elif jogador == 'PEDRA' and escolha == 'Tesoura':
    print('PARABÉNS Você VENCEU!! Eu escolhi Tesoura.')

elif jogador == 'PAPEL' and escolha == 'Papel':
    print('Foi um EMPATE!! \nEu também escolhi Papel.')
elif jogador == 'PAPEL' and escolha == 'Tesoura':
    print('Você PERDEUU!! \nEu escolhi Tesoura.')
elif jogador == 'PAPEL' and escolha == 'Pedra':
    print('Você VENCEU!! Eu escolhi Pedra.')

elif jogador == 'TESOURA' and escolha == 'Tesoura':
    print('Foi um EMPATE!! \nEu também escolhi Tesoura.')
elif jogador == 'TESOURA' and escolha == 'Pedra':
    print('Você PERDEUU!! \nEu escolhi Pedra.')
elif jogador == 'TESOURA' and escolha == 'Papel':
    print('Você VENCEU!! Eu escolhi Papel.')

else:
    print('\033[31m----------ERRO!!---------\033[m')
print('-='*10)
"""
from random import randint
from time import sleep
#Outra forma de fazer isso com o GB
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(0.8)
print('KEN')
sleep(0.8)
print('PÔ')
print('-='*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)
if computador == 0:  #Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador VENCEU')
    elif jogador == 2:
        print('Jogador PERDEU')
    else:
        print('Jogada Invalida')
elif computador == 1:  #Computador jogou PAPEL
    if jogador == 0:
        print('Jogador PERDEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador VENCEU')
    else:
        print('Jogada Invalida')
elif computador == 2:  #Computador jogou TESOURA
    if jogador == 0:
        print('Jogador VENCEU')
    elif jogador == 1:
        print('Jogador PERDEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada Invalida')
