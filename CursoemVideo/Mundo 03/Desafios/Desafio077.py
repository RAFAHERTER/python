'''palavras = ('aprender', 'programar', 'linguagem',
            'python', 'curso','gratis', 'estudar',
            'praticar', 'trabalhar', 'mercado',
            'programador', 'futuro')
for c in range(len(palavras)):
    print(f'\nNa palavra {palavras[c]} temos ', end='')
    for x in range(len(palavras[c])):
        if palavras[c][x] in 'aeiou':
            print(f'{palavras[c][x]}' , end=' ')
'''
#COM GB
palavras = ('aprender', 'programar', 'linguagem',
            'python', 'curso','gratis', 'estudar',
            'praticar', 'trabalhar', 'mercado',
            'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
#MDS, ele faz parecer fácil e simples kkkkkkkk
#Demorei muito para pensar nisso.

