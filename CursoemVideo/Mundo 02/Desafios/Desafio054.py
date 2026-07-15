from datetime import date
atual = date.today().year
q = 0
j = 0
for c in range(1, 8):
    data = int(input('Digite o ano de nascimento: '))
    if atual - data < 21:
        q = q +1
    else:
        j = j +1
print('Existem {} menores de idade e {} maiores de idade'.format(q, j))