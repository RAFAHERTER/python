'''
Crie um programa que leia nome, ano de nascimento e
carteira de trabalho e cadastre-os (com idade) em
um dicionário se por acaso a CTPS for diferente
de 0, o dicionário receberá também o ano de
contratação e o salário. Calcule e acrescente, além
da idade, com quantos anos a pessoa vai se aposentar.

#SOZINHO

from datetime import date
ano_atual = date.today().year
dicionario = dict()

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

'''
from datetime import datetime
dados = dict()
dados["Nome"] = input('Nome: ')
nascimento = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['CTPS'] != 0:
    dados['contratação']= int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 35) - datetime.now().year
print('-='*30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')

