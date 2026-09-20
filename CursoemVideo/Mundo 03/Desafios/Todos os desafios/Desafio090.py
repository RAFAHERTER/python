'''
Faça um programa que leia nome e média de um aluno.
Guardando também a situação num dicionário.
No final, mostre o conteúdo de estrutura na tela.

#SOZINHO

dicionario = dict()
dicionario['Nome'] = input('Nome: ').title()
dicionario['Média'] = float(input('Média: '))
print(f'Nome é igual a {dicionario["Nome"]}')
print(f'Média é igual a {dicionario["Média"]}')

if dicionario['Média'] >= 7:
    dicionario['Situação'] = 'Aprovado'
    print(f'Situação é igual a {dicionario["Situação"]}')
else:
    dicionario['Situação'] = 'Reprovado/Recuperação'
    print(f'Situação é igual a {dicionario["Situação"]}')


'''
#COM GB
aluno = dict()
aluno['nome'] = input('Nome: ').title()
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-='*30)
for k, v in aluno.items():
    print(f'  -{k} é igual a {v}')

