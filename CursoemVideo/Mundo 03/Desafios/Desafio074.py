'''from random import randint
sorteado = randint(1, 10)
sorteado2 = randint(1, 10)
sorteado3 = randint(1, 10)
sorteado4 = randint(1, 10)
sorteado5 = randint(1, 10)
tupla = sorteado, sorteado2, sorteado3, sorteado4, sorteado5
maior = sorted(tupla)[-1]
menor = sorted(tupla)[0]
print(tupla)
print(f'O maior número é o {maior}')
print(f'O menor número é o {menor}')
'''
#COM GB
from random import randint
numeros = (randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10),
     randint(1, 10))
print(f'Os valores sorteados foram: ', end= '')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi: {max(numeros)}')
print(f'O menor valor sorteado foi: {min(numeros)}')
