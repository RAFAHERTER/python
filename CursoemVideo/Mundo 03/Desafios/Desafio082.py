'''lista = list()
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

'''
#COM GB
num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-='*30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')


