'''
Faça um programa que tenha uma função chamada 'escreva()'
que receba um texto qualquer como parâmetro e mostre uma
mensagem com tamanho adaptável.

#SOZINHO
def escreva(frase):
    print('~'*(len(frase) + 3))
    print(frase.center(len(frase) ))
    print('~'*(len(frase) + 3))

escreva('   CURSO DE PYTHON')
escreva('   CURSO DE PYTHON NO YOUTUBE')
escreva('   SEI LA')
escreva('   OLÁ MUNDO!!')

'''
#COM GB
def escreva(msg):
    tamanho = len(msg) + 4
    print('~'*tamanho)
    print(msg.center(tamanho)) #Não tem no vídeo esse comando 'center'
    print('~'*tamanho)


#Programa Principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')

