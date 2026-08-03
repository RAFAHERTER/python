lista = []
dados = []
while True:
    dados.append(input('Nome: '))
    notas = list()
    nota1 = int(input('Nota 1: '))
    nota2 = int(input('Nota 2: '))
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
    print(f'{c[0]} ', end='')
    print(f'{c[2]:>20} ', end='')
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

