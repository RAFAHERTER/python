num = int(input('Digite um número inteiro positivo: '))
contador = 0
print(int(num), end=' -> ')
while num != 1 :
    if num % 2 == 0:
        contador += 1
        num = num / 2
        print(int(num), end=' -> ')
    else:
        contador += 1
        num = num * 3 + 1
        print(int(num), end=' -> ')
print('FIM')
print('Foram necessários {} passos até chegar em 1'.format(contador))
