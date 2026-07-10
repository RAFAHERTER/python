#Praticando com cores no pyhton
print('\033[3;33;44m Olá, Mundo! \033[m ') #Não importa a sequência que for usar
print('\033[1m Olá, Mundo!')
nome = 'Rafael Herter'

cores = {'limpa':'\033[m', #Criação de variável
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',}

print('Olá, muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))

