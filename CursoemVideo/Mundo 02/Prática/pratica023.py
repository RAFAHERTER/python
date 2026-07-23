print('Olá, sou um caixa de banco')
saque = int(input('Digite o valor do saque: (R$) '))
print('O seu saque foi de R${}.00'.format(saque))
resto = saque
if saque // 100 >= 1:
    qtt_100 = saque //100
    print('Será necessário {} notas de 100 reais'.format(qtt_100))
    resto = saque % 100
if resto // 50 >= 1:
    qtt_50 = resto // 50
    print('Será necessário {} notas de 50 reais'.format(qtt_50))
    resto = resto % 50
if resto // 20 >= 1:
    qtt_20 = resto // 20
    print('Será necessário {} notas de 20 reais'.format(qtt_20))
    resto = resto % 20
if resto // 10 >= 1:
    qtt_10 = resto // 10
    print('Será necessário {} nota(s) de 10 reais'.format(qtt_10))
    resto = resto % 10
if resto // 5 >=1:
    qtt_5 = resto // 5
    print('Será necessário {} nota(s) de 5 reais'.format(qtt_5))
    resto = resto % 5
if resto // 2 >= 1:
    qtt_2 = resto // 2
    print('Será necessário {} nota(s) de 2 reais'.format(qtt_2))

