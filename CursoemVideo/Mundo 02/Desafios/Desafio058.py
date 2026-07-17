from random import randint
print('-=-'*20)
print('Vou pensar em um número entre 0 e 10')
aleatorio = randint(0, 10)
palpite = ''
tentativas = 0
while palpite != aleatorio:
    palpite = int(input('Em que número eu pensei? '))
    if palpite != aleatorio:
        print('Errou tente novamente! ')
    tentativas += 1
print('PARABÉNS!! Você acertou e precisou de {} tentativas'.format(tentativas))
