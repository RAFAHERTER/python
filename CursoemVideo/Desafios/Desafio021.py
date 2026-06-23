import pygame #Infelizmente o pygame ainda não está disponível para essa versão do python, sendo ela a mais morderna até o momento
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play('ex021.mp3')
pygame.event.wait()