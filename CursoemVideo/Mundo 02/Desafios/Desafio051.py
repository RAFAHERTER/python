print('-----'*10)
print('             PROGRESSÃO ARITIMÉTICA           ')
print('-----'*10)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1) * razao #DECIMO termo da PA
for c in range (primeiro,decimo + razao , razao):
    print('{} ' .format(c), end='')
print('ACABOU')