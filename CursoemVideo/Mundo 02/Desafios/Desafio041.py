ano = int(input('Digite o ano de nascimento: '))
if ano > 2026:
    print('-=-' *10, '\033[31mERRO!!\033[m', '-=-' *10)
idade = 2026 - ano
if idade <= 9:
    print('Você tem {} anos e é um'.format(idade))
    print('Nadador MIRIM')
elif 9 < idade <= 14:
    print('Você tem {} anos e é um'.format(idade))
    print('Nadador INFANTIL')
elif 14 < idade <= 19:
    print('Você tem {} anos e é um'.format(idade))
    print('Nadador JUNIOR')
elif 19 < idade <= 20:
    print('Você tem {} anos e é um'.format(idade))
    print('Nadador SÊNIOR')
elif idade > 20:
    print('Você tem {} anos e é um'.format(idade))
    print('Nadador MASTER')
else:
    print('-=-' *10, '\033[31mERRO!!\033[m', '-=-' *10)
