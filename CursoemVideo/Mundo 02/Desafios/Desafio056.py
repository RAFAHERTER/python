soma = 0
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

