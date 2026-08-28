'''
Crie um dicionário 'alunos' onde a chave é o nome do aluno e o valor é 
outro dicionário com nota1, nota2, nota3. Cadastre 3 alunos, calcule 
a média de cada um e mostre quem está aprovado (média >= 6) e quem está 
reprovado.

'''
alunos = {   }
notas = {    }
lista = list()
soma = media = 0
while True:
    nome = str(input('Nome: '))

    for c in range(0, 3):
        n = float(input(f'Nota {c + 1}: '))
        lista.append(n)
        soma += n
        notas[f'Nota {c + 1}'] = n
    media = sum(lista) / len(lista)
    alunos[nome] = notas
    alunos['Média'] = media
    
    escolha = input('Quer continuar? [S / N]: ').strip().upper()
    while True:
        if escolha not in 'SN':
            print('ERRO!! Digite apenas "S" ou "N".')
            escolha = input('Quer continuar? [S / N]: ').strip().upper()
        if escolha in 'SN':
            break
    if escolha in 'N':
        break

print(alunos)
