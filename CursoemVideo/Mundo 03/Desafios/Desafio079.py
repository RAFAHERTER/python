lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    for conteudo in lista:
        if lista.count(conteudo) > 1:
            lista.remove(conteudo)
            print('Valor duplicado! Não vou adicionar...')
        else:
            print('Valor adicionado com sucesso...')
    escolha = input('Quer continuar? [S/N] ').strip().upper()[0]
    while escolha not in 'SN':
        escolha = input('Quer continuar? [S/N] ').strip().upper()[0]
    if escolha in 'N':
        break
lista.sort()
print(f'Você digitou os valores {lista}')


