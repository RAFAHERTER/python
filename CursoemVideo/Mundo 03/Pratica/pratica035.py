import random
lista = ['Rafael', 'Guilherme', 'Ettore', 'Larissa', 'Alexandre',
        'Ana', 'Beatriz', 'Gabriel', 'Lucas', 'Bruna']
random.shuffle(lista)

meio = len(lista) // 2

time1 = lista[:meio]
time2 = lista[meio:]

    
print(f'O primeiro time é {time1}')

print(f'O segundo time é {time2}')
