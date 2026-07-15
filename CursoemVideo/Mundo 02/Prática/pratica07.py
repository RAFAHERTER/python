velho = 0
novo = 0
nome_velho = 0
nome_novo = 0
for c in range(1, 4):
    nome = str(input('Digite seu nome: '))

    idade = int(input('Qual é a sua idade? '))
    if c == 1:
        nome_velho = nome
        nome_novo = nome
        velho = idade
        novo = idade
    else:
        if idade > velho:
            nome_velho = nome
            velho = idade
        if idade < novo:
            nome_novo = nome
            novo = idade
print('O mais novo tem {} anos e se chama {}'.format(novo, nome_novo))
print('O mais velho tem {} anos e se chama {}'.format(velho, nome_velho))
