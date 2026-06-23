import random

al1=input('Digite o nome do aluno(a): ')
al2=input('Digite o nome do aluno(a): ')
al3=input('Digite o nome do aluno(a): ')
al4=input('Digite o nome do aluno(a): ')

alunos=[al1,al2,al3,al4]
random.shuffle(alunos)

print('A ordem de sequência para as apresentações é \n{}; '
      '\n{}; \n{}; \n{}.'.format(alunos[0], alunos[1], alunos[2], alunos[3]))