'''
Faça um programa que tenha uma função chamada 'escreva()'
que receba um texto qualquer como parâmetro e mostre uma
mensagem com tamanho adaptável.

'''


def escreva(frase):
    print('~'*(len(frase) + 3))
    print(frase.center(len(frase) ))
    print('~'*(len(frase) + 3))

escreva('   CURSO DE PYTHON')
escreva('   CURSO DE PYTHON NO YOUTUBE')
escreva('   SEI LA')
escreva('   OLÁ MUNDO!!')


