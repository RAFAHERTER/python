'''
#Trabalhando com variáveis compostas (TUPLAS)
#Quando eu tenho uma variável simples, e no final do código eu coloco o mesmo nome da variável, ela vai sobrescrever a variável anterior.

#É possível fazer uma variável composta, que é uma variável que guarda mais de um valor, e nesse caso, a variável composta é a TUPLA.

#Variável simples - Armazena apenas um valor
#Variável composta - Armazena mais de um valor

lanche = ('hamburguer','suco', 'pizza', 'pudim')
#            '0'        '1'      '2'     '3'
#Para 'pegar' um valor da tupla, eu preciso colocar o nome da variável e o índice do valor que eu quero pegar.

print(lanche[1: 3]) #Vai imprimir o valor do índice 1, que é 'suco'e o 2 que é a 'pizza', mas não vai imprimir o valor do índice 3, que é o 'pudim'. pois o índice 3 não está incluso no intervalo.

#Se printar 'lanche ' vai imprimir todos os valores da tupla, e não apenas um valor específico.

print(lanche) 

print(lanche[-1]) #Vai imprimir o  ultimo valor, que é o 'pudim'.

print(lanche[-2]) #Vai imprimir o valor do índice -2, que é a 'pizza'.

print(len(lanche)) #Vai imprimir a quantidade de valores que tem na tupla, que nesse caso é 4.

print(sorted(lanche)) #Vai imprimir os valores da tupla em ordem alfabética, mas não vai alterar a tupla original.

print(lanche[1:]) #Vai imprimir todos os valores da tupla a partir do índice 1, que é o 'suco', até o final da tupla.

print(lanche[:3]) #Vai imprimir todos os valores da tupla até o índice 3, que é o 'pudim', mas não vai imprimir o valor do índice 3.


#AS TUPLAS SÃO IMUTÁVEIS, OU SEJA, NÃO É POSSÍVEL MUDAR OS VALORES DE UMA TUPLA, MAS É POSSÍVEL ADICIONAR NOVOS VALORES A UMA TUPLA.

for c in lanche:
    print(c) #Vai imprimir todos os valores da tupla, um por linha.

#Coloando em prática
#Podemos representar tuplas, lista, dicionário, com (), [] ou {}, respectivamente.

lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita' #Nas tuplas não precisa colocar os ().
#Manipulação de tuplas.
print(lanche[-1])
print(lanche[1:3])
print(lanche[0::2]) #De dois em dois. Segue as mesmas regras de fatiamente de string.
#lanche[1] = 'Refrigerante' - comando impossível. Tentativa de substituir um dos valores da TUPLA

for comida in lanche: #mais simples
    print(f'Eu vou comer {comida}')

for posicao, comida in enumerate(lanche): #Caso queira a posição tem que fazer desse jeito nesse caso.
   print(f'Eu vou comer {comida}, na posição {posicao}')

for cont in range(0, len(lanche)): #Sempre que eu precisar da posição esse 'for' é mais efetivo
    print(f'Eu vou comer {lanche[cont]}, na posição {cont}')

# 3 formas de escrever
print('Comi pra caramba')

print(sorted(lanche)) #Organizado em ordem alfabética. O resultado disso é uma lista

a = 2, 5, 4
b = 5,8,1,2
c = b + a
print(c) #Juntar os elementos. Obs: A ordem tem total influência.
print(f'Tem {len(c)} elementos')
print(f'Tem {c.count(5)} "cincos" na tupla')
print(f'O 8 esta na posição {c.index(5, 1)}') # Em que posição está o 8.
#Para número repetidos, ele pega a primeira ocorrência. Caso queira a segunda opção, utiliza aquele ', 1'


'''
pessoa = ('Gustavo', 39, 'M', 99) #Posso colocar diversos tipos de informações dentro de uma tupla.
print(pessoa)
del(pessoa) #Apaga da memória do computador. Posso apagar uma tupla inteira, porém não posso deletar um item da tupla.

