'''
Interrompendo laços de REPETIÇÃO com break

n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
s -= 999
print('A soma vale {}'.format(s))
#Como fazer esse exemplo sem que eu precise fazer essa gambiarra.

'''
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s))
#As f strings
print(f'A soma vale {s}') #Funciona da mesma maneira
