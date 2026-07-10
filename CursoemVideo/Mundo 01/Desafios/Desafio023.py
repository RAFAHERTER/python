'''num = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
num3= num // num2
resto = num % num2
print('O resultado da divisão inteira entre {} e {} é igual a {} e resta {}'.format(num,num2,num3, resto))'''

#----------------FEITO SOZINHO-----------------
"""valor= int(input('Digite um número: '))
print('Unidades: {}'.format(valor%10))
print('Dezenas: {}'.format(valor//10 % 10))
print('Centenas: {}'.format(valor//100 % 10))
print('Milhares: {}'.format(valor//1000 % 10))
print('Dezenas de Milhares: {}'.format(valor//10000 % 10))
print('Centenas de Milhares: {}'.format(valor//100000 % 10))"""

#-----------------------------------------------

#--------------COM GUSTAVO GUANABARA-----------------
""""num= int(input('Digite um número: '))
n= str(num)
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(n[3])) #Dígito 4
print('Dezenas: {}'.format(n[2])) #Dígito 3
print('Centenas: {}'.format(n[1])) #Dígito 2
print('Milhares: {}'.format(n[0])) #Dígito 1"""""
#Obs: Maneira errada, pois ele da erro quando digitado um número que não tenha 4 dígitos.

num= int(input('Digite um número: '))
u= num // 1 % 10
d= num // 10 % 10
c= num // 100 % 10
m= num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezenas: {}'.format(d))
print('Centenas: {}'.format(c))
print('Milhares: {}'.format(m))
#Basicamente o que eu havia feito estava correto, porém não havia feito com outras variáveis.
#O que faria com que o código ficasse menos complicado.
