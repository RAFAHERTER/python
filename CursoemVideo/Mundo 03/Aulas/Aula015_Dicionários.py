"""
INTRODUZINDO OS DICIONÁRIOS

Diferente das listas que tinha que referenciar
um elemento através da sua posição. Os
dicionários referenciam por nomes, letras ou
palavras.

Nos dicionários nós podemos personalizar os
índices.

TUPLA: ()
LISTAS: []
DICIONÁRIOS: {}

dados = [ 'Pedro', 25]
dados = dict()
dados = {'nome': 'Pedro', 'idade': 25}}

Agora não é possível dar print(dados[0])
ou print(dados[1])

Tenho que dar print(dados[nome]
print(dados[idade]

Caso queira adicionar algum elemento não
precisa utilizar o 'append', pois não funciona
posso simplesmente fazer :
dados['sexo'] = 'M' #Irá criar um novo elemento
com nome 'sexo' e vai colocar o 'M' dentro dele
Tudo de forma automática.

Também funciona para remover elementos.
Utilizando o comando 'del'
del dados['idade']

Assim irá perder o elemento juntamente com os
valores nele embutidos.

Ex:
filme = {'título': 'Star Wars',
        'ano': 1977,
        'diretor': 'George Lucas'
    }
O python chama esses elementos de chaves, ou melhor,
de 'keys'

VALOR

    print(filme.values())
    retornará
    Star Wars, 1977, George Lucas

CHAVE

print(filme.keys())

    retornará
    título
    ano
    diretor

ITEM

    print(filme.items())
    retornará
    OS DOIS

filme = {
    'titulo' : 'Star Wars',
    'ano' : 1977,
    'diretor' : 'George Lucas'
}
for k, v in filme.items():
    print(f'{k}: {v}')

#PRÁTICA
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['nome'] = 'Leandro' #Também posso modificar os valores.
pessoas['peso'] = 85.0
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
del pessoas['sexo']
for k, v in pessoas.items():
    print(k, '=', v)

#

brasil = list()
estado1 = {'Uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'Uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['Uf'])

#

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #As cópias do dicionário é impossível fazer através de um fatiamento completo
#Por isso, utiliza-se o método 'copy()'
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()

"""
dicionario = {'jogador 1' : 4, 'jogador 2': 6, 'jogador 3':2}
resultado = sorted(dicionario.items(), key = lambda item: item[1])
print(resultado)
