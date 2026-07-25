insira = int(input('Digite um valor entre 0 e 20: '))
extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
       'Quatorze', 'Quinze', 'Dezesseis', 'Desessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    if insira < 0 or insira > 20:
        print('Tente novamente.', end=' ')
        insira = int(input('Digite um valor entre 0 e 20: '))
    if 0 <= insira < 20:
        break
print(f'Você digitou o número {extenso[insira]}')

