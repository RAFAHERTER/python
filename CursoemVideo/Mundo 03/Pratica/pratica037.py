def eh_primo(numero):
    tot = 0
    primo = False
    for c in range(1, numero + 1):
        if numero % c == 0:
            tot += 1
    if tot == 2:
        primo = True
        lista.append(numero)
    else:
        primo = False
    return primo

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[31mERRO!! DIGITE APENAS NÚMEROS INTEIROS\033[m')

        if ok:
            break
    return valor


#Programa Principal
lista = list()
num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}')
eh_primo(num)
for c in range(0, 101):
    eh_primo(c)
print(lista)

