print('Falta pouco para finalizar a sua COMPRA!!')
compra = float(input('Digite o valor final do carrinho: '))
pagamento = str(input('Qual a forma de pagamento? ')).strip().lower()

if pagamento == 'dinheiro' or pagamento == 'cheque':
    desconto = compra - (compra * 0.10)
    print('Sua compra tem um desconto de 10%, devendo pagar um valor de R${:.2f}'.format(desconto))
elif pagamento == 'debito' or pagamento == 'débito' or  pagamento == 'credito' or pagamento == 'crédito':
    desconto = compra - (compra * 0.05)
    print('Sua compra tem um desconto de 5%, devendo um valor de R${:.2f}'.format(desconto))
elif pagamento == 'parcela 2x':
    print('O valor a ser pago deverá ser {}, SEM DESCONTO!'.format(compra))
elif pagamento == 'parcela 3x':
    juros = compra + (compra * 0.20)
    print('Será acrescido um juros de 20% do valor.\n'
          'E deverá ser cobrado {:.2f} da compra.'.format(juros))
