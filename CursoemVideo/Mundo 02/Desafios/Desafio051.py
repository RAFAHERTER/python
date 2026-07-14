p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
for c in range (p,r * 10 , r):
    print('{}, ' .format(c), end='')
