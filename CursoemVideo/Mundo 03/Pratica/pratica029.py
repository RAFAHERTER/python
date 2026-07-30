numeros = (3, 8, 15, 22, 7, 40, 11, 6, 19, 24)
pares = list()
impares = list()
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'Lista par: {pares}')
print(f'Lista impar: {impares}')

