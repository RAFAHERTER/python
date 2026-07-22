'''#Refazendo o código, pois estava errado.
num = int(input('Digite um número: '))
escolha = input('Deseja continuar? [S/N] ').strip().upper()
soma = int(0)
media = 0
contador = 0
maior = 0
menor = 0
if escolha != 'S' and escolha != 'N':
    print('Opção invalida! Tente novamente.')
elif escolha == 'S':
    while escolha == 'S':
        contador += 1
        soma += num
        media = soma / contador
        num = int(input('Digite um número: '))
        escolha = input('Deseja continuar? [S/N] ').strip().upper()
elif escolha == 'N':
    contador += 1

print('A média entre os {} valores é igual a {}'.format(contador, media))
print('O maior valor é o {}'.format(maior))
print('O menor valor é o {}'.format(menor))
'''
#Com o GB
resposta = 'S'
media = soma = contador = maior = menor = 0
while resposta in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    contador += 1
    if contador == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]

media = soma / contador
print('Você digitou {} números, e a média foi de {}'.format(contador, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))

