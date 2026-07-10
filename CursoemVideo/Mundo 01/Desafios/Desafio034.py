print('---------Desafio 034--------')
print('--'*10)
salario = float(input('Digite o seu salario:R$ '))
if salario >= 1250:
    aumento = salario + (salario * 10 / 100)
    print('O seu salário teve um aumento de 10%\n'
          'Com resultado final de R${:.2f}'.format(aumento).replace('.',','))
else:
    aumento = salario + (salario * 15 / 100)
    print('O seu salário teve um aumento de 15%\n'
          'Com resultado final de R${:.2f}'.format(aumento).replace('.',','))
