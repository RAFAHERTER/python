nome = str(input('Digite seu nome completo: ')).strip()
print('Analisnado seu nome...')
print('Seu nome em maiúsculas: {}'.format(nome.upper()))
print('Seu nome em minúsculas: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) #Podemos também usar o replace (' ', '').
print('O primeiro nome é {} e tem {} letras'. format(nome.split()[0],len(nome.split()[0])))
print('E o último nome é {} e tem {} letras'.format(nome.split()[-1], len(nome.split()[-1])))
'''
Podemos usar o seguinte código para encontrar a quantidade de letras do primeiro nome
print(nome.find(' ')) #isto é, falar qual a posição do primeiro espaço que tem.
Assim irá mostrar exatamente a quantidade de letras que possuí.
'''