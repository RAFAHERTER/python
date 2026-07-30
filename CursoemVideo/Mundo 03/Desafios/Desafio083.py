frase = input('Diga uma frase: ')
if frase.count('(') == frase.count(')'):
    print('Essa expressão é válida')
elif frase.count('(') == frase.count(')') == 0 or frase.count('(') != frase.count(')'):
    print('Essa expressão não é válida.')

