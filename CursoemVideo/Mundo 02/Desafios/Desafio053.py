'''frase = input('Digite uma frase qualquer: ')
frase2= frase.strip().replace(' ', '').upper()
inverso = frase2[::-1]
print('O inverso da frase {} é {}'.format(frase2, inverso))
if frase2 == inverso:
    print('Isto É um Palíndromo')
else:
    print('Isto NÃO É um palíndromo')
    '''
#EXISTE OUTRO JEITO DE FAZER ISSO, SEM O 'FOR', Que na minha concepção, é mais simples.
#Com Gustavo Guanabara
#Ele fez basicamente o mesmo que eu, porém ele splitou a frase
# E também juntou com join. DESSE JEITO:
frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):#preciso pegar a última letra, vai até a primeira letra, e o último -1 é pra pegar o inverso
    inverso += junto[letra]
if inverso == junto:
    print('Temos um Palíndromo.')
else:
    print('Não é um palíndromo.')
    