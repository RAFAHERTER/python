frase = ''
while frase != 'M' and frase != 'F':
    frase = input('Digite seu sexo: ').strip().upper()
    print('Estrutura inválida, tente novamente!')
print('Seu sexo é {}'.format(frase))
