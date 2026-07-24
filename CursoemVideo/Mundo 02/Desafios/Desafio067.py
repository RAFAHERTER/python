num = 0
cont = 0

while True:
    print('--'*15)
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('--' * 15)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c:2} = {num * c}')

print('Programa tabuada encerrado!! Volte sempre!')