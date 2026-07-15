soma = 0
cont = 0
for c in range(1, 501, 2 ):
    if c % 3 == 0:
        cont = cont + 1 #Contar quantos números tem
        soma = soma + c #Acumulador dos valores.
print('O somatório de todos os {} valores solicitados é {}'.format(cont, soma))
