lista = [ ]
dados = []
while True:
    dados.append(input('Nome: '))
    dados.append(input('Numero de telefone: '))
    dados.append(input('Cidade que nasceu: '))
    lista.append(dados[:])
    dados.clear()
    escolha = input('Quer continuar? [S/N] ').strip().upper()[0]
    while escolha not in 'SN':
        escolha = input('Quer continuar? [S/N] ').strip().upper()[0]
    if escolha in 'N':
        break
print('--'*30)
for pos, c in enumerate(lista):
    print(f'{pos:<4} {c[0]:<8}')

while True:
    print('--' * 30)
    dados_num = int(input('Gostaria de saber os dados de qual contato? [999 interrompe] '))
    if dados_num == 999:
        break
    if dados_num <= len(lista):
        print(f'Número de {lista[dados_num][0]} ', f'é {lista[dados_num][1]}'
           f'\nE Nasceu em {lista[dados_num][2]}')

