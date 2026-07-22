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