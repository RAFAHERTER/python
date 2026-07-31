lista = list()
lista_prioridade = list()
while True:
    nome = input('Digite um nome: '). strip()
    if nome[0] == '*':
        lista_prioridade.append(nome[1:])
    else:
        if nome == 'sair':
            break
        lista.append(nome)
    
lista_completa = lista_prioridade + lista
print(lista_completa)

