#Estrutura aninhada. Tem esse nome, pois é essa estrutura uma dentro da outra.
nome = str(input('Qual seu nome? ')).strip().upper()
if nome == 'RAFAEL':
    print('Que nome bonito você tem {}!'.format(nome.title()))
elif nome == 'RAFA':
    print('Seu nome é bem popular no brasil, {}.'.format(nome.title()))
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia {}.'.format(nome.title()))
