dia=int(input('Quantos dias o carro foi alugado? '))
km=float(input('Quantos quilomêtros foram rodados? '))
preco= dia*60 + km*0.15
print('O preço a ser pago pelo aluguel do carro será'
      'de R${:.2f}'.format(preco) .replace('.',','))
