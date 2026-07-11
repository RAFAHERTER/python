from time import sleep
print('\033[34m-\033[m'*30)
print('\033[31mBanco de Empréstimos para casas.\033[m')
print('\033[34m-\033[m'*30)
casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? '))
anos = int(input('Quantos anos de financiamento? '))
mensalidade = casa / (anos * 12)
print('Processando...')
sleep(0.5)

if mensalidade <= (salario * 0.3):
    print('Você\033[1;34m PODE\033[m fazer o financiamento para essa casa.\n'
          'E terá que pagar a mensalidade de\033[1;36m R${:.2f}\033[m por \033[1;35m{}\033[m anos'.format(mensalidade, anos))
else:
    print('\033[31mEmpréstimo NEGADO!!\033[m')
