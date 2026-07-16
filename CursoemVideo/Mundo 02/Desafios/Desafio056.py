'''soma = 0
velho = 0
novo = 0
nome_velho = 0 #Terei que mudar as variáveis
nome_novo = 0
total = 4
mulher = 0
achou_homem = False
for c in range(1, 5):
    nome = str(input('Qual é o nome da {}ª pessoa? '.format(c)))
    sexo = input('Qual é o sexo da {}ª pessoa? (M/F) '.format(c)).upper().strip()
    idade = int(input('Qual é a idade da {}ª pessoa? '.format(c)))
    if sexo == 'F' and idade < 20:
        mulher += 1
    soma += idade
    if sexo == 'M':
        if not achou_homem:
            nome_velho = nome
            nome_novo = nome
            velho = idade
            novo = idade
            achou_homem = True
        else:
            if idade > velho:
                nome_velho = nome
                velho = idade
            if idade < novo:
                nome_novo = nome
                novo = idade
media = soma  / total
print('A média das idades desse grupo é {}'.format(media))
if achou_homem:
    print('O homem mais velho é o {} com {} anos'.format(nome_velho, velho))
else:
    print('Não há homens no grupo.')
print('Existe(m) {} mulher(es) abaixo de 20 anos'.format(mulher))
'''
#COM GUSTAVO GUANABARA
soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
mulher_menor = 0
for p in range(1, 5):
    print('------ {}ª PESSOA ------'.format(p))
    nome =input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F]').strip().upper()
    soma_idade += idade
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo == 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo == 'F' and idade < 20:
        mulher_menor += 1
media_idade = soma_idade / 4
print('A média de idade do grupo é de {} anos'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}'.format(maior_idade_homem, nome_velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher_menor))
