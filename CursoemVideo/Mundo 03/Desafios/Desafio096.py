'''
Faça um programa que tenha uma função chamada
'area()', que receba as dimensões de um terreno
retangular (largura e comprimento) e mostre a área
do terreno.

'''
def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área do terreno é igual a {a}m²')
area(float(input('Qual a largura do terreno? (m) ')),
     float(input('Qual a comprimento do terreno? (m) ')))

