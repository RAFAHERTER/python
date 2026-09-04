"""
Modularização = Ato de construir módulos

Sistemas cada vez maiores.
Porém existe programas que exigem vários outros arquivos

Foco: Dividir um programa grande em partes
Aumentar a legibilidade.

Programas com muitas linhas, tendem a ficar difíceis de
enxergar onde possa fazer possíveis alterações.

Facilita a manutenção do programa.

Vantagens de se ter modularização:
Organização do código
Reaproveitamento de código em outros projetos
Facilita manutenção do programa
Ocultação do código detalhado (detalhes de implementação)

#TEORIA + PRÁTICA

def fatorial(numero):
    f = 1
    for c in range(1, numero + 1):
        f *= c
    return f

def leiaInt(msg):
    while True:
        valor = input(msg)
        if valor.isnumeric():
            break
        else:
            print('ERRO!! Digite apenas números inteiros: ')
    return int(valor)

def dobro(numero):
    return numero * 2

def triplo(numero):
    return numero*3 

#Podemos pegar uma função de outro arquivo .py, desde que esteja no mesmo diretório. Assim as funções podem ser reaproveitadas em outros programas, sem precisar reescrever o código. Isso é chamado de Modularização.

#E como podemos fazer a ligação entre os arquivos? Através do comando import. hahahaha incrível né?


import uteis #Nome do arquivo que contém as funções que queremos importar. O nome do arquivo deve ser o mesmo do arquivo .py, sem a extensão .py. E o arquivo deve estar no mesmo diretório do arquivo que está importando.

#Caso existe outro arquivo com o mesmo nome de função, o Python vai dar preferência para a útlima função importada. Então, se você importar um arquivo com uma função que já existe no seu arquivo, a função do arquivo importado vai sobrescrever a função do seu arquivo.

num = uteis.leiaInt('Digite um valor: ')
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}')
dobro_num = uteis.dobro(num)
print(f'O dobro de {num} é {dobro_num}')
triplo_num = uteis.triplo(num)
print(f'O triplo de {num} é {triplo_num}')


"""
#PACOTES - CONCEITO
 #E se dentro do arquivo úteis, existisse muitas funções a ponto de eu precisar de muitos módulos com funções. Assim a gente pode criar uma pasta que contenha todos os arquivos com funções separadas por assuntos. Isto é, uma pasta com vários arquivos .py com diversas funções sobre diferentes assuntos. E essa pasta é chamada de PACOTE. E para que o Python reconheça essa pasta como um pacote, precisamos criar um arquivo chamado __init__.py dentro da pasta. Esse arquivo pode estar vazio, mas ele precisa existir para que o Python reconheça a pasta como um pacote.
from uteis import numeros #Importando o pacote uteis e o módulo numeros dentro do pacote uteis. Assim podemos acessar as funções dentro do módulo numnumeros

num = numeros.leiaInt('Digite um valor: ')
fat = numeros.fatorial(num)

print(f'O fatorial de {num} é {fat}')

dobro_num = numeros.dobro(num)

print(f'O dobro de {num} é {dobro_num}')

triplo_num = numeros.triplo(num)

print(f'O triplo de {num} é {triplo_num}')


