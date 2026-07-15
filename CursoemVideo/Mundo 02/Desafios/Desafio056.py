soma = 0
velho = 0
novo = 0
nome_velho = 0 #Terei que mudar as variáveis
nome_novo = 0
total = 4
mulher = 0
for c in range(1, 5):
    nome = str(input('Qual é o nome da {}ª pessoa? '.format(c)))
    sexo = input('Qual é o sexo da {}ª pessoa? (M/F) '.format(c)).upper().strip()
    idade = int(input('Qual é a idade da {}ª pessoa? '.format(c)))
    if sexo == 'F' and idade < 20:
        mulher += 1
    soma += idade
    if c == 1:
        nome_velho = nome  # NOME
        nome_novo = nome  # NOME
        velho = idade  # IDADE
        novo = idade  # IDADE




    else:
        if idade > velho:
            nome_velho = nome
            velho = idade
        if idade < novo:
            nome_novo = nome
            novo = idade



media = s  / total
print('A média das idades desse grupo é {}'.format(media))
print('O homem mais velho é o {} com {} anos'.format(nome_velho, velho))
print('A pessoa mais jovem é o(a) {} com {} anos'.format(nome_novo, novo))
print('Existem {} mulheres abaixo de 20 anos'.format(mulher))
