velocidade = int(input('Qual a velocidade do carro? ').strip())

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Diminua a velocidade!! Você foi multado!')
    print('Sua multa será de R${},00'.format(multa))
else:
    print('Parabéns!! Mantenha na velocidade permitida.')
