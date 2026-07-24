print('='*30)
print('BANCO DO CURSO EM VIDEO')
print('='*30)
saque = int(input('Qual valor você quer sacar? R$ '))
resto = saque
tot100 = 0
if saque // 100 >= 1:
    qntt_100 = saque // 100
    print(f'Total de {qntt_100} cédula(s) de R$100.00')
    resto = saque % 100
if resto // 50 >= 1:
    qntt_50 = resto // 50
    print(f'Total de {qntt_50} cédula(s) de R$50.00')
    resto = resto % 50
if resto // 20 >= 1:
    qntt_20 = resto // 20
    print(f'Total de {qntt_20} cédula(s) de R$20.00')
    resto = resto % 20
if resto // 10 >= 1:
    qntt_10 = resto // 10
    print(f'Total de {qntt_10} cédula(s) de R$10.00')
    resto = resto % 10
if resto // 5 >= 1:
    qntt_5 = resto // 5
    print(f'Total de {qntt_5} cédula(s) de R$5.00')
    resto = resto % 5
if resto // 2 >= 1:
    qntt_2 = resto // 2
    print(f'Total de {qntt_2} cédulas(s) de R$2.00')
    resto = resto % 2
if resto // 1 >= 1:
    qntt_1 = resto // 1
    print(f'Total de {qntt_1} moeda(s) de R$1.00')
    resto = resto % 1
print('='*30)
print('Volte sempre ao Banco CEV')