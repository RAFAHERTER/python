print('Sou um identificador de números primos')
num = int(input('Digite um número: '))
contador = 0
if num == 0 or num == 1:
    print('O número {} não é primo'.format(num))
for c in range(1, num+1):
    if num % c == 0:
        contador += 1
if contador > 2 :
    print('O número {} não é primo'.format(num))
if contador == 2:
    print('O número {} é primo'.format(num))
