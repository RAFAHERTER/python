palavra = input('Digite uma palavra: ').strip().lower()
vogais = 0
for c in range(len(palavra)):
    if palavra[c] in 'aeiou':
        vogais += 1

print('A soma de todas as vogais na frase é {}'.format(vogais))
