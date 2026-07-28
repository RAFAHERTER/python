alunos = (
('Ana', 7.5, 8.0),
('Bruno', 4.0, 5.5),
('Carla', 9.0, 9.5),
('Diego', 6.0, 6.5)
)
media = 0
nota1 = 1
nota2 = 2
for c in range(len(alunos)):
    media = (alunos[c][nota1] + alunos[c][nota2]) / 2
    if media >= 6.0:
        print(f'O(A) aluno(a) {alunos[c][0]} teve media {media:.2f}. APROVADO!!')
    else:
        print(f'O(A) aluno(a) {alunos[c][0]} teve media {media:.2f}. REPROVADO!!')

