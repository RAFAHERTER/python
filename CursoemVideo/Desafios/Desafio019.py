import random
aluno1=str(input('Digite o nome do primeiro aluno(a): '))
aluno2=str(input('Digite o nome do segundo aluno(a): '))
aluno3=str(input('Digite o nome do quarto aluno(a): '))
aluno4=str(input('Digite o nome do quinto aluno(a): '))
alunos=[aluno1,aluno2,aluno3,aluno4] #Criar uma lista no python é feito entre colchetes.
sorteado=random.choice(alunos)

print('O aluno sorteado para limpar o quadro pro professor é o(a) {}'
      .format(sorteado))