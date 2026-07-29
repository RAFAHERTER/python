'''
Estudo de LISTAS []
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
#Como faço para transformar o lanche[3] (pudim)
#em picolé?
#Com tuplas isso é impossível.
#Para isso é necessário utilizar as LISTAS.

lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
lanche[3] = 'picolé'
#Diferente das TUPLAS, as LISTAS são MUTÁVEIS

lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
lanche[3] = 'picolé'
lanche.append('cookie') #Adiciona um elemento a lista
lanche.insert(0, 'cachorro quente')
#O insert serve para colocar um elemento dentro da posição que deseja
print(lanche)


lanche = ['hamburguer', 'suco', 'pizza', 'pudim']

#Adicionando elementos na lista

lanche[3] = 'picolé'
lanche.append('cookie') #Adiciona um elemento a lista
lanche.insert(0, 'cachorro quente')
#O insert serve para colocar um elemento dentro da posição que deseja
print(f'Adicionando elementos na lista \n{lanche}')

#Apagando elementos na lista

del lanche[3] #Tirei o elemento na posição 3 (pizza)
lanche.pop(3) #Outra maneira de apagar um elemento de uma lista
#lanche.pop() #elimina obrigatóriamente o último elemento
lanche.remove('cookie') #Indica o valor que quer eliminar da lista

if 'cachorro' in lanche: #Com o if eu verifico se é possível
    lanche.remove('cachorro') #Se tentar remover algo que não está na lista, é retornado um erro.
print(lanche)

#Criar listas através de 'range'

valores = list(range(4, 11)) #Cria uma lista pelo comando list, com os valores definidos
print(valores)
lista = [8, 2, 5, 4, 9, 3, 0]
print(f'Lista aleatória {lista}')
lista.sort() #Muda a lista deixando-a ordenada. Diferente das TUPLAS que apenas mostra ordenada. Na lista ela é alterada.
print(f'A mesma lista com o comando .sort() {lista}')
lista.sort(reverse=True)
print(f'Lista em ordem decrescente {lista}')
print(len(lista))

#Prática
num = [2, 5, 9, 1]
print(f'Lista sem alterações: {num}')
num[2]= 3 #Listas são mutáveis!!
num.append(7)

num.insert(2, 0) #Na posição 2, insira o valor 0
num.pop() #Remove o último valor
num.sort() #Crescente
print(f'Lista com alterações ordem crescente: {num}')

num.sort(reverse=True)#Decrescente
print(f'Lista em ordem decrescente {num}')
print(f'Essa lista tem {len(num)} elementos')
num.pop(3) #Elimina o 3° elemento
print(num)

#

num = [2, 5, 9, 1]
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
num.remove(9) #Remove apenas o 1° elemento que aparece, se houver mais elementos iguais, assim permanecerão.
print(num)

#

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei {v}!!!')
print('Cheguei ao final da lista')

#

a = [2, 3, 4, 7]
b = a
b[2] = 8 #No python as listas fazem uma ligação entre si, Portanto se eu igualar uma lista e tentar modificar UMA delas
#Irei modificar as duas LISTAS. FAÇAM seus TESTES!
print(f'Lista A: {a}')
print(f'Lista B: {b}')

#

a = [2, 3, 4, 7]
b = a[:] #Se eu mando todos os valores de 'a', agora sim a situação muda.
#Pois agora eu estou pegando uma cópia dos VALORES de 'a' e não uma cópia da lista
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
'''

