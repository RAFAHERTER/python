from random import randint
from time import sleep
numero = randint(0, 5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5 Tente acertar...')
print('-=-'*20)
chute= (int(input('Em que número eu pensei? ')))
print('PROCESSANDO...')
sleep(1) #Pausa o programa fazendo-o esperar por x segundos
if chute == numero:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI!! Eu pensei no número {} e não no {}'.format(numero, chute))
