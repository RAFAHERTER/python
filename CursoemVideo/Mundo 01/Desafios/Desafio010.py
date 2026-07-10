num=float(input('Digite o valor que possuí '
                'na carteira: R$'))
dolar= num/3.27
print('Você que possuí {} reais na carteira, \n'
      'convertidos em dólares, você tem {:.2f} dólares'
      .format(num, dolar))