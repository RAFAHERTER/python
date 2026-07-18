'''print('-'*30)
print('Sequência de FIBONACCI' .center(30))
print('-'*30)
num = int(input('Quantos termos deseja mostrar: '))
primeiro = 1
segundo = 0
terceiro = 0
contador = 0
while contador != num:
    contador += 1
    terceiro = segundo + primeiro
    primeiro = segundo
    segundo = terceiro
    print('{} -> '.format(primeiro), end='')
'''
#Com GB
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos deseja mostrar: '))
primeiro = 0
segundo = 1
print('~'*30)
print('{} -> {}'.format(primeiro, segundo), end='')
cont = 3
while cont <= n:
    terceiro = primeiro + segundo
    print(' -> {}'.format(terceiro), end='')
    primeiro = segundo
    segundo = terceiro
    cont += 1
print(' -> FIM')

