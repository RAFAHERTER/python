'''
Crie um programa onde o usuário possa digitar
7 valores numéricos
e cadastre-os em uma lista única que
mantenha separados os valores pares
e impares. No final mostre os valores pares
e impares em ordem crescente

#SOZINHO

completa = [ [] , [] ]
for c in range(0, 7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        completa[0].append(num)
    else:
        completa[1].append(num)
completa[0].sort()
completa[1].sort()
print(f'Os valores pares digitados foram: {completa[0]}')
print(f'Os valores ímpares foram: {completa[1]}')
'''
#Com GB
num = [ [], [] ]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-='*30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram {num[0]}')
print(f'Os valores ímpares  foram {num[1]}')

