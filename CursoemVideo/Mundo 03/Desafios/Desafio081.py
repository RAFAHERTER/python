lista = list()
while True:
    cinco_encontrado = False
    lista.append(int(input('Digite um valor: ')))
    escolha = input('Quer continuar? [S/N] ').strip().upper()[0]
    while escolha not in 'SN':
        escolha= input('Quer continuar? [S/N] ').strip().upper()[0]
    if escolha == 'N':
        break
lista.sort(reverse=True)
lista.count(5)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O valor 5 apareceu na lista na(s) posições(s) ', end=' ')
    for pos, c in enumerate(lista):
        if c == 5:
            print(pos, end=' ')
else:
    print('O valor 5 não foi encontrado na lista.')

