'''lista = list()
num = 0
while True:
    num = (int(input('Digite um valor: ')))
    if num in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(num)
        print('Valor adicionado com sucesso...')
    escolha = input('Quer continuar? [S/N] ').strip().upper()[0]
    while escolha not in 'SN':
        escolha = input('Quer continuar? [S/N] ').strip().upper()[0]
    if escolha in 'N':
        break
lista.sort()
print(f'Você digitou os valores {lista}')

'''
#Com GB
numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resposta = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resposta in 'N':
        break
print('-='*30)
numeros.sort()
print(f'Você digitou os valores {numeros}')

