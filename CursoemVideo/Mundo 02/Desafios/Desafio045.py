import random
print('Vamos jogar JOKENPÔ')
lista = ['Pedra', 'Papel', 'Tesoura']
escolha = random.choice(lista)
jogador = input('Escreva aqui a sua esolha: ').strip().upper()

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