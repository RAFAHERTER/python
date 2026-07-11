peso = float(input('Digite seu peso: '))
altura= float(input('Digite sua altura: '))
imc = peso / pow(altura,2)
if 0 < imc <= 18.5:
    print('Seu Índice de Massa Corpórea é {:.2f}'.format(imc))
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Seu Índice de Massa Corpórea é {:.2f}'.format(imc))
    print('Peso ideal.')
elif 25 <= imc < 30:
    print('Seu Índice de Massa Corpórea é {:.2f}'.format(imc))
    print('Sobrepeso')
elif 30 <= imc <= 40:
    print('Seu Índice de Massa Corpórea é {:.2f}'.format(imc))
    print('Obesidade')
elif imc > 40:
    print('Seu Índice de Massa Corpórea é {:.2f}'.format(imc))
    print('Obesidade mórbida')
else:
    print('\033[31m------------ERRO!!-------------\033[m')