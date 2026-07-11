nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Infelizmente você foi \033[31mREPROVADO!\033[m\n'
          'Boa sorte no próximo ano.')
elif 5 < media < 6.99:
    print('Você está de \033[33mRECUPERAÇÃO\033[m e \n'
          'necessita de mais notas para ser'
          ' \033[34mAPROVADO!\033[m \nBoa sorte na prova'
          'de recuperação.')
elif 7 <= media <= 10:
    print('PARABÉNS!!\n'
          'Você foi \033[34mAPROVADO!!\033[m')
else:
    print('\033[31mERRO!!\033[m')
