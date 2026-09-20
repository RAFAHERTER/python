'''lista = list()
while True:

    lista.append(int(input('Digite um valor: ')))
    escolha = input('Quer continuar? [S/N] ').strip().upper()[0]
    while escolha not in 'SN':
        escolha= input('Quer continuar? [S/N] ').strip().upper()[0]
    if escolha == 'N':
        break
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O valor 5 apareceu na lista na(s) posições(s) ', end=' ')
    for pos, c in enumerate(lista):
        if c == 5:
            print(pos, end=' ')
else:
    print('O valor 5 não foi encontrado na lista.')

'''
valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = input('Quer continuar? [S/N] ')
    if resp in 'Nn':
        break

print('-='*30)
print(f'Você digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 apareceu na lista.')
else:
    print('O valor 5 não foi encontrado na lista')

