total_maior = 0
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

