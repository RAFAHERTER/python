def moeda_dobro(valor, formatar=False):
    """
    Retorna o dobro do valor fornecido.
    
    :param valor: O valor a ser dobrado.
    :param formatar: Se o resultado deve ser formatado como moeda.
    :return: O dobro do valor.
    """
    if formatar:
        return f"R$ {valor * 2:.2f}"
    return valor * 2

def moeda_metade(valor, formatar=False):
    """
    Retorna a metade do valor fornecido.
    
    :param valor: O valor a ser dividido pela metade.
    :param formatar: Se o resultado deve ser formatado como moeda.
    :return: A metade do valor.
    """
    if formatar:
        return f"R$ {valor / 2:.2f}"
    return valor / 2

def aumentar(valor, percentual, formatar=False):
    """
    Aumenta o valor fornecido em um determinado percentual.
    
    :param valor: O valor a ser aumentado.
    :param percentual: O percentual de aumento.
    :param formatar: Se o resultado deve ser formatado como moeda.
    :return: O valor aumentado.
    """
    if formatar:
        return f"R$ {valor + (valor * percentual/100):.2f}"
    return valor + (valor * percentual/100)

def diminuir(valor, percentual, formatar=False):
    """ 
    Diminui o valor fornecido em um determinado percentual.
    
    :param valor: O valor a ser diminuído.
    :param percentual: O percentual de diminuição.
    :param formatar: Se o resultado deve ser formatado como moeda.
    :return: O valor diminuído.
    """
    if formatar:
        return f"R$ {valor - (valor * percentual/100):.2f}"
    return valor - (valor * percentual/100)