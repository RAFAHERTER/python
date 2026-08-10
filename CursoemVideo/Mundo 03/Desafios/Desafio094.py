'''
ENUNCIADO:
Crie um programa que leia nome, sexo, idade de várias pessoas
guardando os dados de cada pessoa num dicionário e todos os
dicionários numa lista. No final mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade.
C) Uma lista com as mulheres
D) Uma lista com idade acima da média.

#SOZINHO

lista_completa = list()
dicionario = dict()
lista_mulher = list()
acima_media = list()
soma_idade = 0
while True:
    dicionario['Nome'] = str(input('Nome: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    dicionario['Sexo'] = sexo
    idade = int(input('Idade: '))
    if sexo in 'F':
        lista_mulher.append(dicionario['Nome'])
    dicionario['Idade'] = idade
    soma_idade += idade
    lista_completa.append(dicionario.copy())
    escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if escolha in 'N':
        break
media_idade = soma_idade / len(lista_completa)
print(lista_completa)
print('-='*30)
print(f'-O grupo tem {len(lista_completa)} pessoas')
print(f'-A média das idades é {media_idade:.2f} anos')
print(f'-As mulheres cadastradas foram {lista_mulher}')
print('-Lista de pessoas que estão acima da média da idade: ')
for c in lista_completa:
    for k, v in c.items():
        if c['Idade'] >= media_idade:
            acima_media.append(c.items())
            print(f'{k} = {v};', end=' ')
    print()

print('<< ENCERRADO >>')
'''
#COM GB
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Responda apenas S ou N.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta == 'N':
        break
print('-='*30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas') #Letra A
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos') #Letra B
print('As mulheres cadastradas forma ', end='') #Letra C
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}', end=' ')
print()
print('Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
        print()
print('  <<ENCERRADO>>  ')


