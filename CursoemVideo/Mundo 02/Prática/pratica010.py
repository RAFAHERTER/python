nota1 = float(input('Digite sua 1ª nota: '))
nota2 = float(input('Digite sua 2ª nota: '))
nota3 = float(input('Digite sua 3ª nota: '))
if not 0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10:
    print('As notas precisam ser, obrigatóriamente entre 0 e 10!'
          '\nPor favor, tente novamente!')
else:
    valor_nota1 = nota1 * 2
    valor_nota2 = nota2 * 3
    valor_nota3 = nota3 * 5
    media_p = (valor_nota1 + valor_nota2 + valor_nota3)/ 10
    print('A média ponderada das suas notas equivalem a {:.2f}'.format(media_p))
    if 5 <= media_p <= 10:
        print('PARABÉNS!! Você conseguiu passar para o próximo semestre!!')
    elif 0 < media_p < 5:
        print('INFELIZMENTE você não conseguiu atingir a nota necessária para passar de semestre!!')
    else:
        print('''Pontuação incoerente!! 
    A média final tem que estar compreendida entre 0 e 10.
    Por favor verifique os dados inseridos e tente novamente!''')
