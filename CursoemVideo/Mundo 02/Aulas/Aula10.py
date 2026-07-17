'''
ESTRUTURA DE REPETIÇÃO COM TESTE LÓGICO
Trabalhando com 'while' (LEIA 'ENQUANTO')
Nós usamos while para casos em que é
desconhecido o seu final / limite.
Enquanto no 'for' usamos:
'Vai de um limite até outro limite'
o while usa:
vai de um determinado ponto até o infinito
até alguma coisa acontecer.
OU SEJA, vai repetir a quantidade de vezes
necessária enquanto NÃO cumprir com a
determinação estabelecida.

- Escrevendo em python
while not 'maçã': #maçã é o condicional do 'while'
    passo
pega
for c in range(1, 10):
    print(c)
print('FIM')

c = 1
while c < 10:
    print(c)
    c = c + 1
print('FIM')

n = 1
while n != 0: #Condição de parada. Obtenho o poder de controlar de parar
    n = int(input('Digite um valor: '))
print('FIM')
'''
#PRÁTICA
n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} número ímpares'.format(par, impar))


