'''valor = contador = soma = 0
while valor != 999:
    valor = int(input('Digite um número (999 para parar): '))
    if valor == 999:
        break
    soma += valor
    contador += 1
print(f'Foram digitados {contador} números \n'
      f'e a soma entre eles é {soma}')
'''
#Com GB
soma = contador = 0
while True:
    numero = int(input('Digite um valor (999 para parar): '))
    if numero == 999:
        break
    soma += numero
    contador += 1
print(f'A soma dos {contador} valores foi {soma}')

