lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    escolha = input('Quer continuar? [S/N] ').strip().upper()[0]
    while escolha not in 'SN':
        escolha = input('Quer continuar? [S/N] ').strip().upper()[0]
    if escolha == 'N':
        break
par = list()
impar = list()
for c in lista:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'Sua lista completa: {lista}')
print(f'Sua lista par: {par}')
print(f'Sua lista impar: {impar}')

