#---------Condições Aninhadas------------
"""
Geralmente surge a partir de situações que possuem
mais de duas possibilidades.

carro.siga()
se (if) carro.esquerda:()
    carro.siga()
    carro.direita()
    carro.siga()
    carro.direita()
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
senão se (elif) carro.direita:()
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.siga()
senão (else):
    carro.siga()
carro.pare()

if carro.esquerda():
    [BLOCO 1]

elif carro.direita():
    [BLOCO 2]

elif carro.esquerda():
    [BLOCO 3]:

else:
    [BLOCO 4]:

"""

