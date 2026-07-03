#--------ESTRUTURAS CONDICIONAIS ----------------
"""tempo = int(input('Quantos anos tem seu carro? '))

if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')


print('--FIM--')


#Condição simplificada
tempo = int(input('Quantos anos tem seu carro? '))
print('Carro novo' if tempo <= 3 else 'Carro velho')
print('--FIM--')"""
nome = str(input('Digite seu nome: '))
if nome == 'Rafael':
    print('Que nome lindo você tem!!') #O python trabalha estritamente com identação. Portanto, é de extrema importância
    #Que o que estiver dentro da condição seja separado pela identação, caso contrário não irá executar o comando quando
    #Realizado
else:
    print('Seu nome é tão normal')

#Todo comando que estiver colado dentro do lado esquerdo, será executado!
print('Bom dia, {}!!'.format(nome))