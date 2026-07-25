'''total_maior = 0
tot_homem = 0
mulher_menor = 0
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper().strip()

    if sexo not in 'MmFf': #Validação de entrada
        while True:
            sexo = input('Sexo [M/F]: ').upper().strip()
            if sexo in 'MmFf':
                break

    if idade >= 18:
        total_maior += 1
    if sexo == 'M':
        tot_homem += 1
    if sexo == 'F' and idade < 20:
        mulher_menor += 1
    continuar = input('Quer continuar? [S/N] ').upper().strip()

    if continuar not in 'NnSs':
        while True:
            continuar = input('Quer continuar? [S/N] ').upper().strip()
            if continuar in 'NnSs':
                break
    if continuar == 'N':
        break
print('-'*30)
print(f'O total de pessoas cadastradas com mais de 18 anos é de {total_maior}.')
print(f'Fora cadastrado(s) {tot_homem} homem(ns).')
print(f'Fora(m) cadastrada(s) {mulher_menor} mulher(es) menores de 20 anos.')
'''
#Com GB
tot18 = tot_homem = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo [M/F]: ').strip()).upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        tot_homem += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resposta = ' '
    while resposta not in 'SsNn':
        resposta = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resposta == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {tot_homem} homens cadastrados.')
print(f'E temos {totM20} mulher menor de 20 anos.')

