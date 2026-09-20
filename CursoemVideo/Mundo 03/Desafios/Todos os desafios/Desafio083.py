'''frase = input('Diga uma frase: ')
if frase.count('(') == frase.count(')'):
    print('Essa expressão é válida')
elif frase.count('(') == frase.count(')') == 0 or frase.count('(') != frase.count(')'):
    print('Essa expressão não é válida.')

'''
#COM GB - Utilizando listas(Diferente de minha pessoa)
expr = str(input('Diga uma expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')

