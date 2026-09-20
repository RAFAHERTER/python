"""
Enunciado:
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.
"""
from Pasta_Desafios import moeda

valor = float(input('Digite um valor: R$ '))

print(f'O dobro de {valor} é R$ {moeda.moeda_dobro(valor):.2f}')

print(f'A metade de {valor} é R$ {moeda.moeda_metade(valor):.2f}')

print(f'O valor {valor} aumentado em 10% é R$ {moeda.aumentar(valor, 10):.2f}')

print(f'O valor {valor} diminuído em 10% é R$ {moeda.diminuir(valor, 10):.2f}')