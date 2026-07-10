num = int(input('Digite um número: '))
print('Escolha a base de conversão do número digitado '
      'para uma das opções abaixo:\n'
      'Binário\n'
      'Octal\n'
      'Hexadecimal')
escolha = input('').strip().upper()

if escolha == 'BINÁRIO' or escolha == 'BINARIO':
    binario = bin(num)[2:]
    print('O número {} em binários é {}'.format(num, binario))
elif escolha == 'OCTAL':
    octal = oct(num)[2:]
    print('O número {} em octal é {}'.format(num, octal))
elif escolha == 'HEXADECIMAL':
    hexadecimal = hex(num)[2:]
    print('O número {} em hexadecimal é {}'.format(num, hexadecimal))
else:
    print('Opção inválida. Escolha Binário, Octal ou Hexadecimal.')