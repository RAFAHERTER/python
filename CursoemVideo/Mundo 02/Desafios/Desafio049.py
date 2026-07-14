num = int(input('Digite um número: '))
print('-' *20)
for c in range(1,11):
    #print(f'{num} x {c} = {num*c}') JEITO que o pycharm recomendou-me
    print('{} X {:2} = {}'.format(num,c,num*c))
print('-' * 20)
