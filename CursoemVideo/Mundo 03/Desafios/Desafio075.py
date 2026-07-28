num1 = int(input('Digite o 1° valor: '))
num2 = int(input('Digite o 2° valor: '))
num3 = int(input('Digite o 3° valor: '))
num4 = int(input('Digite o 4° valor: '))
tupla = num1, num2, num3, num4
cont_9 = tupla.count(9)
pos_3 = 0
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {cont_9} vezes')
if tupla.count(3) != 0:
    pos_3 = tupla.index(3) + 1
    print(f'O primeiro valor 3 apareceu na {pos_3}° posição.')
else:
    print('O valor 3 não apareceu nenhuma vez.')

cont_pares = 0
print('Os valores pares digitados são: ', end = '')
for c in tupla:
    if c % 2 == 0:
        cont_pares += 1
        print(c, end=' ')
if cont_pares == 0:
    print('Nenhum valor par encontrado')
