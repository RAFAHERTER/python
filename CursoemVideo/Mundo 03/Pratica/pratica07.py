numero = (5, 12, 8, 130, 44, 3, 77, 21)
maior = 0
menor = 0
for c in range(len(numero)):
    if c == 0:
        maior = numero[c]
        menor = numero[c]
    else:
        if numero[c] > maior:
            maior = numero[c]
        if numero[c] < menor:
            menor = numero[c]
print(f'O maior número é {maior} e o menor é {menor}')

