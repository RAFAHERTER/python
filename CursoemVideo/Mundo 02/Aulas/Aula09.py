"""
ESTRUTURA DE REPETIÇÃO COM VARIÁVEL DE CONTROLE
Nova categoria de estrutura de controle: LAÇOS, REPETIÇÕES OU ITERAÇÃO.
Os laços são representados para estruturas de repetições
fazendo com o programa se repita, evitando várias linhas
com comandos repetitivos.

"""


#for c in range (1, 6, 2): #Pula de 2 em 2
 #   print('Oi')
#print('FIM')

#for c in range (6, 0, -1): #Caso queira decrescente, '-1'
   # print(c)
#print('FIM')

#num = int(input('Digite um valor: '))
#for c in range (0, num +1, 2):
    #print(c)

#i = int(input('Início: '))
#f = int(input('Fim: '))
#p = int(input('Passo: '))
#for c in range(i, f+1, p):
 #   print(c)
#print('Fim')

s = 0
for c in range(1, 4):
    n = int(input('Digite um valor: '))
    s += n #Ou s = s + n, refere-se ao valor da variável repetidas vezes somadas com os próximos valores a ser inserido.
print('O somatório de todos os valores foi {}'.format(s))