dicionario = dict()
dicionario['Nome'] = input('Nome: ').title()
dicionario['Média'] = float(input('Média: '))
print(f'Nome é igual a {dicionario["Nome"]}')
print(f'Média é igual a {dicionario["Média"]}')

if dicionario['Média'] >= 7:
    dicionario['Situação'] = 'Aprovado'
    print(f'Situação é igual a {dicionario["Situação"]}')
else:
    dicionario['Situação'] = 'Reprovado'
    print(f'Situação é igual a {dicionario["Situação"]}')

