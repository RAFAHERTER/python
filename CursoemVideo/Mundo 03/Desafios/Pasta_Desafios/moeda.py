def moeda_dobro(valor):
    """
    Retorna o dobro do valor fornecido.
    
    :param valor: O valor a ser dobrado.
    :return: O dobro do valor.
    """
    return valor * 2

def moeda_metade(valor):
    """
    Retorna a metade do valor fornecido.
    
    :param valor: O valor a ser dividido pela metade.
    :return: A metade do valor.
    """
    return valor / 2

def aumentar(valor, percentual):
    """
    Aumenta o valor fornecido em um determinado percentual.
    
    :param valor: O valor a ser aumentado.
    :param percentual: O percentual de aumento.
    :return: O valor aumentado.
    """
    return valor + (valor * percentual/100)

def diminuir(valor, percentual):
    """ 
    Diminui o valor fornecido em um determinado percentual.
    
    :param valor: O valor a ser diminuído.
    :param percentual: O percentual de diminuição.
    :return: O valor diminuído.
    """
    return valor - (valor * percentual/100)