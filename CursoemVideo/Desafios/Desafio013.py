num=float(input('Qual o valor do salário? '))
aumento= num + (num*15/100)
print('Parabéns!! \nO valor do seu salário'
      ' teve um aumento de 15%!!\nO valor bruto '
      'do seu salário atual é de {:.2f}'
      .format(aumento))