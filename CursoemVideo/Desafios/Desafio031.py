d = int(input('Qual a distância da viagem em Km? '))
preco = d * 0.50 if d <= 200 else d * 0.45 # Outra maneira de realizar. Porém, não gostei kkkkk
"""if d <=200:
    preco = float(d * 0.5)
else:
    preco = float(d * 0.45)"""

print('O preço da passagem para a viagem é R${}'.format(preco))