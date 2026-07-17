from time import sleep
num1 = int(input('Insira um número inteiro: '))
num2 = int(input('Insira outro número inteiro: '))
escolha = 0
while escolha != 6:

    print('''O que você gostaria de fazer com os números?
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] menor
[ 5 ] novos números
[ 6 ] sair''')
    escolha = int(input('Sua escolha: '))
    if escolha <= 0 or escolha > 6:
        while escolha <= 0 or escolha > 6:
            escolha = int(input('Opção inválida! Tente novamente: '))
    if escolha == 1:
        soma = num1 + num2
        print('A soma dos números inseridos é {}'.format(soma))
    if escolha == 2:
        multiplicar = num1 * num2
        print('A multiplicação dos números inseridos é {}'.format(multiplicar))
    if escolha == 3:
        if num1 > num2:
            maior = num1
            print('O maior número entre eles é o {}'.format(maior))
        elif num1 < num2:
            maior = num2
            print('O maior número entre eles é o {}'.format(maior))
        else:
            print('Os números inseridos são iguais!')
    if escolha == 4:
        if num1 < num2:
            menor = num1
            print('O menor número entre eles é o {}'.format(menor))
        elif num2 < num1:
            menor = num2
            print('O menor número entre eles é o {}'.format(menor))
        else:
            print('Os números são iguais!')
    if escolha == 5:
        print('Você escolheu trocar os números')
        num1 = int(input('Insira um número inteiro: '))
        num2 = int(input('Insira outro número inteiro: '))
    if escolha == 6:
        print('Saindo do programa.')
    sleep(1)
