num = 0
media = 0
soma = 0
contador = 0
maior = 0
menor = 0
escolha = ''
while escolha != 'N':
    contador += 1
    num = int(input('Digite um número: '))
    soma += num
    media = soma / contador
    if contador  == 1:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print('---'*10)
print('Você inseriu {} valores'.format(contador))
print('A média de todos os valores é {:.2f}'.format(media))
print('O maior valor é {}'.format(maior))
print('O menor valor é {}'.format(menor))
print('---Fim do PROGRAMA---')
