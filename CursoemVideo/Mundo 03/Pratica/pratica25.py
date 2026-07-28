numeros = (5,12,8,130,44,3,77,21)
soma = 0
for c in range(0,len(numeros)):
    soma += numeros[c]
media = soma / len(numeros)
print(f'A soma é {soma}')
print(f'E a média é {media}')
