"""nome = str(input('Digite seu nome completo: ')).strip()
print('Muito prazer te conhecer {}!!'.format(nome.split()[0]))
print('O primeiro nome é {}'.format(nome.split()[0]))
print('E o último nome é {}'.format(nome.split()[-1]))"""

#----------COM GB--------------

n = str(input('Digite seu nome completo: ')).strip()
nome= n.split()
print('Muito prazer em te conhecer {}!!'.format(nome[0]))
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[-1]))
