from datetime import date
def voto(ano):
    v = date.today().year - ano
    print(f'Com {v} anos: ', end='')
    if 16 <= v <= 17 or v >= 54:
        print('VOTO OPCIONAL')
    elif v < 16:
        print('NÃO VOTA')
    else:
        print('VOTO OBRIGATÓRIO')
    return v

#Programa Principal
a = int(input('Digite o ano de nascimento: '))
voto(a)

