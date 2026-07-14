frase = input('Digite uma frase qualquer: ')
frase2= frase.strip().replace(' ', '').upper()
inverso = frase2[::-1]


if frase2 == inverso:
    print('{} é um Palíndromo'.format(frase))
else:
    print('{} não é um palíndromo'.format(frase))