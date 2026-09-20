"""
Enunciado:
Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por eles vai ser ou não formatado pela função 'moeda()', desenvolvida no desafio 108.
"""

from Pasta_Desafios import moeda

valor = float(input('Digite um valor: R$ '))

print(f'O dobro de R${valor:.2f} é igual a {moeda.moeda_dobro(valor, True)}')

print(f'A metade de R${valor:.2f} é igual a {moeda.moeda_metade(valor, True)}')

print(f'O valor R${valor:.2f} aumentado em 10% é igual a {moeda.aumentar(valor, 10, True)}')

print(f'O valor R${valor:.2f} diminuído em 13% é igual a{moeda.diminuir(valor, 13, True)}')
