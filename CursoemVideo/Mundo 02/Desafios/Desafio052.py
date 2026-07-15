#Com gustavo guanabara
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} ' .format(c), end='')
print('\n\033[mO número {} foi dividido {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele é primo')
else:
    print('E por isso ele não é primo')

'''print('Sou um computador que lê números primos.')
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
        print('{} não é primo'.format(num))'''
