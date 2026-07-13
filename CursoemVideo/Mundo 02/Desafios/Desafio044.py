print('{:=^40}'.format('LOJAS HERTER'))
preço = float(input('Digite o valor final do carrinho: '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = 0.9 * preço
elif opcao == 2:
    total = 0.95 * preço
elif opcao == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = preço * 1.2
    totalparc = int(input('Quantas parcelas? '))
    parcela  = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalparc, parcela))


print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, total))