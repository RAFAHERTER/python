'''
LISTAS DENTRO DE LISTAS
dados = ['Pedro', 25]
pessoas = list()
pessoas.append(dados[:]) #Adiciono uma cópia de dados, isto é, um fatiamento da estrutura completa de dados.
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[0] [0]) #Estou escolhendo a primeira lista, e o primeiro item da lista.

#Prática

#
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) #Estou criando uma ligação entre as duas listas mesmo que alteradas.
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:]) #Por isso existe a necessidade de fazer uma cópia dela com [:]
print(galera)

#
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

for p in galera:
    print(f'O(a) {p[0]} tem {p[1]} anos de idade.')

#

galera = list()
dado = list()
totmaior = totmenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear() #.clear , limpa a lista inteira deixando-a zerada
print(galera)
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade')

'''

