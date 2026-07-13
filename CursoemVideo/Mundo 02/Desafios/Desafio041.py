from datetime import date
ano = date.today().year
nascimento = int(input('Digite o ano que nasceu: '))
idade = ano - nascimento
print('O atleta tem {} anos'.format(idade))
if ano > 2026:
    print('-=-' *10, '\033[31mERRO!!\033[m', '-=-' *10)

if idade <= 9:
    print('Nadador MIRIM')
elif 9 < idade <= 14: # O '9' NÃO É NECESSÁRIO
    print('Nadador INFANTIL')
elif 14 < idade <= 19: # O '14' NÃO É NECESSÁRIO
    print('Nadador JUNIOR')
elif 19 < idade <= 25:
    print('Nadador SÊNIOR')
elif idade > 25:
    print('Nadador MASTER')
else:
    print('-=-' *10, '\033[31mERRO!!\033[m', '-=-' *10)
