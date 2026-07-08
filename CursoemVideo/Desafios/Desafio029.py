velocidade = float(input('Qual a velocidade do carro? ').strip())

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('MULTADO!! Você excedeu o limite de velocidade de 80km/h')
    print('Você terá que pagar uma multa de R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança!')
