valor = contador = soma = 0
while valor != 999:
    valor = int(input('Digite um número (999 para parar): '))
    if valor == 999:
        break
    soma += valor
    contador += 1
print(f'foram digitados {contador} números \n'
      f'e a soma entre eles é {soma}')

