from datetime import date
ano_atual = date.today().year
dicionario = {}

dicionario['Nome'] = input('Nome: ')
nascimento = int(input('Ano de nascimento: '))
idade = ano_atual - nascimento
dicionario['Idade'] = f'{idade} anos'
carteira = float(input('Carteira de trabalho: (0 não tem) '))

if carteira != 0:
    contrat = int(input('Ano de contratação: '))
    dicionario['contratação'] = f'{contrat} '
    idade_contratada = contrat - nascimento
    dicionario['Salário'] = float(input('Salário: '))
    contribuicao = idade_contratada + 35
    dicionario['Aposentadoria'] = f'{contribuicao} '
else:
    dicionario['CTPS'] = 0
print('-='*30)
for v in dicionario:
    print(f'{v} tem o valor {dicionario[v]}')

