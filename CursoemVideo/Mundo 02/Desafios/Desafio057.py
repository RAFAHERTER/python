'''frase = ''
while frase != 'M' and frase != 'F':
    frase = input('Digite seu sexo: ').strip().upper()
    print('Estrutura inválida, tente novamente!')
print('Seu sexo é {}'.format(frase))'''
#Com GB
#VALIDAÇÃO DE DADOS
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0] #Só a primeira letra
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo:  ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
