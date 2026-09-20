'''lista = list()
for c in range(0, 5):
    num = int(input(f'Digite o {c + 1}° valor: '))
    if c == 0:
        lista.append(num)
        print('Valor adicionado ao final da lista')
    else:
        posicao_encontrada = False
        for pos, conteudo in enumerate(lista):
            if num < conteudo:
                lista.insert(pos, num)
                print(f'Valor adicionado na posição {pos}')
                posicao_encontrada = True
                break
        if not posicao_encontrada:
            lista.append(num)
            print(f'Valor adicionado no final da lista')
print(lista)

'''
#Com GB
lista = []
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista')
    else:
        posicao = 0
        while posicao < len(lista): #Vai de 0 até a última posição da lista
            if num <= lista[posicao]:
                lista.insert(posicao, num)
                print(f'Adicionado na posição {posicao} da lista...')
                break
            posicao += 1
print('-='*30)
print(f'Os valores em ordem foram {lista}')

