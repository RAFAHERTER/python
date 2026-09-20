'''
Faça um programa que tenha uma função chamada
'area()', que receba as dimensões de um terreno
retangular (largura e comprimento) e mostre a área
do terreno.

#SOZINHO

def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área do terreno é igual a {a}m²')


area(float(input('Qual a largura do terreno? (m) ')),
     float(input('Qual a comprimento do terreno? (m) ')))

'''
#COM GB
def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura} x {comprimento} é de {a}m²')

#Programa principal
print('Controle de Terrenos')
print('-'*20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l,c)
#No meu código sozinho, não foi utilizado duas variáveis
#para guardar na memória. Caso fosse necessário,
#eu criaria sim outras variáveis.
