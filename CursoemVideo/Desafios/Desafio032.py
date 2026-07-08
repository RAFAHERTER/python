ano = int(input('Digite um ano qualquer: '))
bi = ano % 4
if bi == 0:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))