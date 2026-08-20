def notas(*nota, sit=False):
    """
Funçõs para analisar notas e situações de vário alunos
    :param nota: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: Dicionário com informações analisadas pelo programa
    """
    print('-' * 30)
    dicionario = dict()
    total = len(dicionario)
    media = sum(nota) / len(nota)
    dicionario['total'] = total
    dicionario['maior'] = max(nota)
    dicionario['menor'] = min(nota)
    dicionario['media'] = f'{media:.2f}'
    if sit == True:
        if 7 <=  media <= 10:
            dicionario['Situação'] = 'Boa'
        elif media >= 5:
            dicionario['Situação'] = 'Razoável'
        else:
            dicionario['Situação'] = 'Ruim'
    return dicionario


resp = notas(5.5, 7, 6, 2, sit = True)
print(resp)