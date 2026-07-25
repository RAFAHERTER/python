from random import randint
'''print('=-'*20)
print('Vamos jogar Par ou Impar')
while True:
    print('=-' * 20)
    valor = int(input('Diga um valor: '))
    escolha = input('Par ou Ímpar? [P/I] ').strip().upper()
    computador = randint(1, 10)
    soma = valor + computador
    if soma % 2 == 0: #Se o resultado for par
        print(f'Você escolheu {valor} e o computador escolheu {computador}. Total deu {soma} é PAR.')
        if escolha == 'P':
            print('Você VENCEU!!')
            print('Vamos jogar novamente...')
        if escolha == 'I':
            print('Você PERDEU!!')
            break
    if soma % 2 == 1:
        print(f'Você escolheu {escolha} e o computador escolheu {computador}. Total deu {soma} é ÍMPAR.')
        if escolha == 'I':
            print('Você VENCEU!!')
            print('Vamos jogar novamente...')
        if escolha == 'P':
            print('Você PERDEU!!')
            break
'''
#Com GB
vitoria = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = input('Par ou impar? [P/I] ').strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total deu {total}', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!!')
            vitoria += 1
        else:
            print('Você PERDEU!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!!')
            vitoria += 1
        else:
            print('Você PERDEU!!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {vitoria} vez(es)')

