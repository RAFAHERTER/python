'''
Enunciado:
Faça um programa que tenha uma função 'notas()' que pode
receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione, também, as docstrings

#SOZINHO

def notas(*nota, sit=False):
    """
Funçõs para analisar notas e situações de vário alunos
    :param nota: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: Dicionário com informações analisadas pelo programa
    """
    print('-' * 30)
    dicionario = dict()
    media = sum(nota) / len(nota)
    dicionario['total'] = len(dicionario)
    dicionario['maior'] = max(nota)
    dicionario['menor'] = min(nota)
    dicionario['media'] = f'{media:.2f}'
    if sit:
        if 7 <=  media <= 10:
            dicionario['Situação'] = 'Boa'
        elif media >= 5:
            dicionario['Situação'] = 'Razoável'
        else:
            dicionario['Situação'] = 'Ruim'
    return dicionario

#Programa Principal
resp = notas(5.5, 7, 6, 2, sit = True)
print(resp)'''

#Com GB
def notas(*n, sit = False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias)
    :param sit:Valor opcional, indicando se deve ou não adicionar a situação
    :return: Dicionário com informações analisadas pelo programa
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['Situação'] = 'Boa'
        elif r['media'] >= 5:
            r['Situação'] = 'Razoável'
        else:
            r['Situação'] = 'Ruim'
    return r

#Programa Principal
resp = notas(5.5, 2.5, 9, 8.5, sit = True)
print(resp)
help(notas)