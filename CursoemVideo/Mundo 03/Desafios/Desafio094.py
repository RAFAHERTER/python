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
