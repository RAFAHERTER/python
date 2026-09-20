'''
Crie um programa que leia nome e duas notas de vários
alunos e guarde tudo numa lista composta. No final
mostre um boletim contendo a média de cada um e
permita que o usuário possa mostrar notas de cada aluno
individualmente.

#SOZINHO

lista = []
dados = []
while True:
    dados.append(input('Nome: '))
    notas = list()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    notas.append(nota1)
    notas.append(nota2)
    dados.append(notas)
    dados.append(media)
    lista.append(dados[:])
    dados.clear()
    escolha = input('Quer continuar? [S/N]').strip().upper()[0]
    while escolha not in 'SN':
        escolha = input('Quer continuar? [S/N]').strip().upper()[0]
    if escolha in 'N':
        break
print('-='*30)
print(f'{"BOLETIM":^30}')
print('-'*30)
print('No.    NOME            MÉDIA')
print('-'*30)
numerico = 0
for c in lista:
    print(numerico, end='    ')
    numerico += 1
    print(f'{c[0]:<20} ', end='')
    print(f'{c[2]} ', end='')
    print()
print('-'*30)
while True:
    detalhe = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if detalhe == 999:
        break
    print(f'Notas de {lista[detalhe][0]} são {lista[detalhe][1]}')
    print('-' * 30)
print('FINALIZANDO...')
print('<<<<VOLTE SEMPRE!>>>>')
'''
#COM GB
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    ficha.append(([nome, [nota1, nota2], media]))
    resp = input('Quer continuar? [S/N]').strip().upper()[0]
    if resp in 'N':
        break
print('-='*30)
print(f'{"No.":<4} {"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8.1f}')
while True:
    print('-'*30)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<<VOLTE SEMPRE!>>>')
