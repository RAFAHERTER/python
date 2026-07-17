from random import randint
print('''Sou seu computador
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
palpite = int(input('Qual o seu palpite? '))
aleatorio = randint(0, 10)
tentativas = 1
while palpite != aleatorio:
    tentativas += 1
    if palpite > aleatorio:
        palpite = int(input('Menos... Tente mais um vez:  '))
    if palpite < aleatorio:
        palpite = int(input('Mais... Tente mais um vez:  '))
print('PARABÉNS!! Você acertou e precisou de {} tentativas'.format(tentativas))
