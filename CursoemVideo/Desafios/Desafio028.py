import random
numero = random.randint(0, 5)

print('Vou pensar em um número entre 0 e 5 \nTente acertar')
chute= (int(input('Digite aqui o seu chute: ')))

if chute == numero:
    print('Voce acertou!!')
else:
    print('Voce errou!!')
