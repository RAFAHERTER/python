print('Sou uma calculadora que faz tabuada de 1 a 10 de qualquer número')
print('=='*20)
num = int(input('Digite um número: '))
for c in range(1, 11):
    print('{} X {:2} = {:3}'.format(num, c, num * c))
