"""
Enunciado:

Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.
"""
from Pasta_Desafios import moeda

valor = float(input('Digite um valor: R$ '))

print(f'O dobro de R${valor:.2f} é igual a R${moeda.moeda_dobro(valor)}')
print(f'A metade de R${valor:.2f} é igual a R${moeda.moeda_metade(valor)}')
print(f'O valor R${valor:.2f} aumentado em 10% é igual a R${moeda.aumentar(valor, 10)}')
print(f'O valor R${valor:.2f} diminuído em 13% é igual a R${moeda.diminuir(valor, 13)}')
