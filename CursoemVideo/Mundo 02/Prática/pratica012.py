from time import sleep
print('Olá! Sou um caixa de super mercado')
sleep(1)
compra = float(input('Insira aqui o valor da sua compra: '))
pagamento = float(input('Qual o valor do seu pagamento em dinheiro? '))
if pagamento < compra:
    deveria = compra - pagamento
    print('Para o cliente realizar a compra é necessário pagar mais R${:.2f}'.format(deveria))
elif pagamento == compra:
    print('Compra realizada com sucesso!')
else:
    troco = pagamento - compra
    print('Compra realizada com sucesso!')
    print('Você tem um troco de R${:.2f}'.format(troco))
    resto = troco
    if troco // 50 >= 1:
        inteira_50 = int(troco // 50)
        resto = troco % 50
        print('Será necessária {} nota(s) de R$50.00.'.format(inteira_50))
    if resto // 20 >= 1:
        inteira_20 = int(resto // 20)
        resto = resto - inteira_20 * 20
        print('Será necessário {} nota(s) de R$20.00'.format(inteira_20))
    if resto // 10 >= 1:
        inteira_10 = int(resto // 10)
        resto = resto - inteira_10 * 10
        print('Será necessário {} nota(s) de R$10.00'.format(inteira_10))
    if resto // 5 >= 1:
        inteira_5 = int(resto // 5)
        resto = resto - inteira_5 * 5
        print('Será necessário {} nota(s) de R$5.00'.format(inteira_5))
    if resto // 2 >= 1:
        inteira_2 = int(resto // 2)
        resto = resto - inteira_2 * 2
        print('Será necessário {} nota(s) de R$2.00'.format(inteira_2))
    if resto // 1 >= 1:
        inteira_1 = int(resto // 1)
        resto = resto - inteira_1 * 1
        print('Será necessário {} moeda(s) de R$1.00'.format(inteira_1))
