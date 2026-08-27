lista = list()
num =  maior = menor = soma = 0
for c in range(0, 5):
    num = input('Digite um número: ')
    lista.append(num)
    soma += num
    if c == 0:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

media = soma / len(lista)
print(f'O maior número da lista é o {maior}')
print(f'E o menor número da lista é o {menor}')
print(f'A média de todos os números da lista é {media}')
