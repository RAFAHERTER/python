'''
TRABALHANDO COM FUNÇÕES

As funções em todas as linguagens de programação
está vinculada a palavra 'ROTINA', algo que você
faz CONSTANTEMENTE.

print()
len()
input()
int()
float()
"Todas essas são funções"

Posso criar também uma função "mostra linha"
Que irá mostrar na tela uma linha.
No python: 'Função' ou 'def'

Nossa missão é criar uma função personalizada no
python, assim suprir a necessidade conforme os
exercícios são feitos

print('-'*30) #ISSO ESTÁ CONSTANTEMENTE APARECENDO NOS EXERCÍCIOS.

Para evitar isso faça:

def mostraLinha(): #Pode escrever qualquer nome de função
    print('-'*30)

#

def linha(): #Está "criando" um comando novo
    print('-'*30) #Esse comando só será executada, quando você chamar ele pelo programa principal


#PROGRAMA PRINCIPAL
linha()
print('CURSO EM VIDEO'.center(30))
linha()
print('APRENDA PYTHON'.center(30))
linha()
print('GUSTAVO GUANABARA'.center(30))
linha()

#PRÁTICA

def mensagem(msg): #O do meio é uma mensagem que irá vir como parâmetro
    print('-'*30)
    print(msg.center(30))
    print('-' * 30)

mensagem('SISTEMA DE ALUNOS')
mensagem('APRENDA PYTHON')

#

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


soma(4, 5)

#

def contador(* num): #O asterisco vai desempacotar os num
    # O usuário vai passar vários parâmetros e vai empacotar tudo dentro de num
    for valor in num:
        print(valor, end=' ')  #Crie várias tuplas com os valores dos parâmetros

    print('FIM')            #E assim eu posso fazer a mesma coisa com tuplas
contador(5, 7, 3, 1, 4)
contador(8, 4, 7)

#

def contador(* num):
    tamanho = len(num)
    print(f'Recebi os valores {num} e são ao todo {tamanho} números')

contador(5, 7, 3, 1, 4)
contador(8, 4, 7)

#

def dobra(lista): #Eu estabeleço uma ligação entre a lista 'valores' e a lista 'lista'
    pos = 0
    while pos < len(lista): #Enquanto a posição for menor que o tamanho da lista
        lista[pos] *= 2
        pos += 1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
'''

