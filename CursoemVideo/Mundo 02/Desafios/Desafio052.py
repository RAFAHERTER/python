print('Sou um computador que lê números primos.')
num = int(input('Digite um número: '))
if num < 2:
    print('{} não é primo'.format(num))
else:
    primo = True
    for c in range(2, num):
        if num % c == 0:
            primo = False
            break
    if primo:
        print('{} é primo'.format(num))
    else:
        print('{} não é primo'.format(num))


