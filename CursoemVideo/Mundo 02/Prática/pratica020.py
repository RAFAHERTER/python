from random import randint
print('Vou pensar em um número entre 1 e 100. Tente adivinhar.')
computador = randint(1, 100)
escolha = 0
contador = 1
while escolha != computador:
    escolha = int(input('Sua escolha: '))
    if escolha > 100 or escolha < 1:
        print('Opção inválida, tente novamente')
        continue
    if escolha > computador:
        contador += 1
        print('Menos')
    elif escolha < computador:
        contador += 1
        print('Mais')
print('PARABÉNS!! você acertou o número que escolhi em {} tentativas'.format(contador))
