num = int(input('Digite um número: '))
print('Escolha a base de conversão do número digitado '
      'para uma das opções abaixo:\n'
      '[ 1 ] converter para BINÁRIO\n'
      '[ 2 ] converter para OCTAL\n'
      '[ 3 ] converter para HEXADECIMAL')
escolha = int(input('Sua opção: '))

if escolha == 1:
    binario = bin(num)[2:] #'0b' Para binário
    print('O número {} em binários é {}'.format(num, binario))
elif escolha == 2:
    octal = oct(num)[2:] #'0o' Para octal
    print('O número {} em octal é {}'.format(num, octal))
elif escolha == 3:
    hexadecimal = hex(num)[2:] #'0x' Para hexadecimal
    print('O número {} em hexadecimal é {}'.format(num, hexadecimal))
else:
    print('Opção inválida. Escolha Binário, Octal ou Hexadecimal.')