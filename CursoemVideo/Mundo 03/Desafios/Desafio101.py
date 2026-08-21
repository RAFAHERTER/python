'''

Enunciado:
Crie um programa que tenha uma função chamada voto() que vai
receber como parâmetro o ano de nascimento de uma pessoa,
retornando uma valor literal indicando se uma pessoa tem
voto NEGADO, OPCIONAL ou OBRIGATIO nas eleições

Será falado nesse exercício sobre ESCOPO DE IMPORTAÇÃO

#Sozinho

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
'''


def voto(ano):
    from datetime import date #Posso importar apenas para dentro da função, economizando a memória.
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com idade {idade} VOTO NEGADO'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com idade {idade} VOTO OPCIONAL'
    else:
        return f'Com idade {idade} VOTO OBRIGATIO'

#Programa Principal
nascimento = int(input('Digite o ano de nascimento: '))
print(voto(nascimento))
