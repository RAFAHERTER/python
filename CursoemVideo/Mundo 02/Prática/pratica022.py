frase = ''
inverso = ''
while frase != 'FIM':
    frase = input('Digite uma frase: ')
    frase2 = str(frase.strip().replace(' ', '').upper())
    if frase2 == 'FIM':
        break
    inverso_frase2 = frase2[::-1]
    inverso = frase[::-1]
    print('O inverso da frase "{}" é "{}"'.format(frase, inverso))
    if inverso_frase2 == frase2:
        print('A frase "{}" é um palíndromo'.format(frase))
    else:
        print('A frase "{}" não é um palíndromo'.format(frase))
    print('-'*30)
print('Fim do programa')
