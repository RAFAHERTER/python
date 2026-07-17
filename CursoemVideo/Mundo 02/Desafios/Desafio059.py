from time import sleep
#num1 = int(input('Insira um número inteiro: '))
#num2 = int(input('Insira outro número inteiro: '))
#escolha = 0
#while escolha != 6:

#    print('''O que você gostaria de fazer com os números?
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] menor
#[ 5 ] novos números
#[ 6 ] sair''')
 #   escolha = int(input('Sua escolha: '))
   # if escolha <= 0 or escolha > 6:
   #     while escolha <= 0 or escolha > 6:
   #         escolha = int(input('Opção inválida! Tente novamente: '))
  #  if escolha == 1:
#        soma = num1 + num2
 #       print('A soma dos números inseridos é {}'.format(soma))
#    if escolha == 2:
  #      multiplicar = num1 * num2
  #      print('A multiplicação dos números inseridos é {}'.format(multiplicar))
  #  if escolha == 3:
  # #         maior = num1
   #         print('O maior número entre eles é o {}'.format(maior))
   #     elif num1 < num2:
   #         maior = num2
   #        print('O maior número entre eles é o {}'.format(maior))
    #    else:
   #         print('Os números inseridos são iguais!')
 #   if escolha == 4:
   #     if num1 < num2:
  #          menor = num1
  #          print('O menor número entre eles é o {}'.format(menor))
  #      elif num2 < num1:
   #         menor = num2
    #        print('O menor número entre eles é o {}'.format(menor))
   #     else:
  #          print('Os números são iguais!')
  #  if escolha == 5:
   #     print('Você escolheu trocar os números')
   #     num1 = int(input('Insira um número inteiro: '))
    #    num2 = int(input('Insira outro número inteiro: '))
   # if escolha == 6:
   #     print('Saindo do programa.')
 #   sleep(1)
#Com GB
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('Qual a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        multiplicar = n1 * n2
        print('O resultado de {} X {} é {}'.format(n1, n2, multiplicar))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('O maior número é o {}'.format(maior))
        elif n2 > n1:
            maior = n2
            print('O maior número é o {}'.format(maior))
        else:
            print('Os valores são iguais')
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção invalida! Tente novamente.')
    sleep(2)
print('Fim do programa! Volte sempre!')