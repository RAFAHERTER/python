from random import randint
print('=-'*20)
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

