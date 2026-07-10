"""frase= str(input('Digite uma frase: ')).strip().replace(' ', '')
print(frase)
print('A letra "a" aparece {} vezes'.format(frase.count('a')))
print('A primeira letra "a" encontra-se na posição {}'.format(frase.find('a')))
print('A última letra "a" encontra-se na posição {}'.format(frase.rfind('a')))"""

#--------------COM GB----------

frase=str(input('Digite uma frase: ')).upper().strip() #Coloca a frase toda em maiúscula
print('A letra "A" aparece {} vezes'.format(frase.count('A'))) #Esse +1 está aí, pois as posições de uma string sempre
#começa com zero "0".
print('A primeira letra "A" aparece na posição {}'.format(frase.find('A')+1))
print('A última letra "A" apareceu na posição {}'.format(frase.rfind('A')+1))
