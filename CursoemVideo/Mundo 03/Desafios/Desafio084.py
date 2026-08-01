'''Faça um programa que leia NOME e peso de
várias pessoas, guardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas

B) Uma listagem com as pessoas mais PESADAS

C) Uma listagem com as pessoas mais LEVES
'''
dados = list()
lista = list()
qtt_pessoas = peso = maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    peso = float(input('Peso: '))
    if qtt_pessoas == 0:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    dados.append(peso)
    qtt_pessoas += 1
    lista.append(dados[:])
    dados.clear()
    resposta = input('Quer continuar? [S/N]').strip().upper()[0]
    while resposta not in 'SN':
        resposta = input('Quer continuar? [S/N]').strip().upper()[0]
    if resposta in 'N':
        break
print('-='*30)
print(f'Foram cadastradas {qtt_pessoas} pessoas.')
print(f'O maior peso foi de {maior}. Peso de ', end=' ') # maior peso
for p in lista:
    if p[1] == maior:
        print(p[0], end=' ')
print(f'\nO menor peso foi de {menor}. Peso de ', end=' ') # menor peso
for p in lista:
    if p[1] == menor:
        print(p[0], end=' ')

