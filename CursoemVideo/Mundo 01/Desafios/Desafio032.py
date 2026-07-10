ano = int(input('Qual ano você quer analisar? '))
bi = ano % 4

if bi == 0 and ano % 100 != 0 or ano % 400 == 0: #Anos bissextos não pegam os múltiplos de 100 que não são múltiplos de 400.
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
