lista = list()
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

