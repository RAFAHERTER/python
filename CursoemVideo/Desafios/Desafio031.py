d = int(input('Qual a distância da viagem em Km? '))
if d <=200:
    preco = float(d * 0.5)
    print('O preço da passagem para a viagem é R${}'.format(preco))
else:
    preco = float(d * 0.45)
    print('O preço da passagem para a viagem é R${}'.format(preco))