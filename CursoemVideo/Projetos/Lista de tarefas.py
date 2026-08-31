'''
Projeto Todo Lista.
- Adicionar tarefa ( descrição + prioridade: alta/ média/ baixa)
- Listar tarefas ordenadas por prioridade
- Marcar tarefa como concluída
- Remover tarefa
- Mostrar estastísticas (pendentes ou concluídas)
- Usar lista de dicionários, pelo menos 3 funções separadas,
loop com menu até escolher "sair".
'''
from time import sleep


def tarefas(msg):
    tamanho = len(msg) + 8
    print('-'*tamanho)
    print(f'{msg.center(tamanho)} ')
    print('-'*tamanho)


def leiaint(msg):
    while True:
        valor = input(msg)
        if valor.isnumeric():
            break
        else:
            print('ERRO!! Digite apenas números inteiros: ')
    return int(valor)


def menu():
    print('-'*70)
    print("""    [ 1 ] - Adicionar tarefa
    [ 2 ] - Listar tarefa
    [ 3 ] - Marcar tarefa como concluída
    [ 4 ] - Remover tarefa
    [ 5 ] - Sair  """)
    print('-'*70)


def listar_tarefas():
    sleep(1)
    if len(afazeres) == 0:
        print('LISTA VAZIA. POR FAVOR COLOCAR UMA TAREFA!')
        return afazeres
    else:
        afazeres_ordenados = sorted(afazeres, key = lambda p: peso_prioridade[p['Prioridade']])
        for pos, c in enumerate(afazeres_ordenados):
            print(f'{pos + 1}° TAREFA : ', end='')
            print(f'{c['Descrição']} - Prioridade {c['Prioridade']} - Situação {c['Situação']}')
            print()
        return afazeres_ordenados

def task(num):
    global afazeres
    descricao = dict()
    if num == 1:
        descricao['Descrição'] = str(input('Descrição da Tarefa: '))
        descricao['Prioridade'] = str(input('Prioridade da Tarefa: '))
        descricao['Situação'] = 'Pendente'
        afazeres.append(descricao.copy())
        descricao.clear()
    if num == 2:
        tarefas('LISTANDO AS TAREFAS')
        sleep(1)
        listar_tarefas()
    if num == 3:
        sleep(1)
        tarefas('TAREFAS PENDENTES?')
        lista_ordenada = listar_tarefas()
        concluido = leiaint('Qual tarefa foi realizada? [APENAS NÚMEROS] ') - 1
        while concluido >= len(lista_ordenada):
            print('ERRO!! Número incompatível com a quantidade de TAREFAS')
            print('POR FAVOR, TENTE NOVAMENTE!!')
            concluido = leiaint('Qual tarefa foi realizada? [APENAS NÚMEROS] ') - 1
        lista_ordenada[concluido]['Situação'] = 'Concluído'
        print('Tarefa marcada como "CONCLUÍDA"')
        sleep(0.6)
        return lista_ordenada

    if num == 4:
        tarefas('REMOVENDO TAREFAS')
        lista_ordenada = listar_tarefas()
        print('-'*70)
        escolha = leiaint('Qual tarefa deseja remover? [Apenas números] ') - 1
        while escolha >= len(lista_ordenada):
            print('ERRO!! Número incompatível com a quantidade de TAREFAS')
            print('POR FAVOR, TENTE NOVAMENTE!!')
            escolha = leiaint('Qual tarefa deseja remover? [APENAS NÚMEROS] ') - 1

        tarefa_escolhida = lista_ordenada[escolha]
        afazeres.remove(tarefa_escolhida)
        print('REMOVENDO TAREFA')
        sleep(1)
        tarefas('TAREFA REMOVIDA COM SUCESSO')
        return lista_ordenada

#Programa Principal
afazeres = list()
peso_prioridade = {'alta' : 1, 'média' : 2, 'baixa': 3}
tarefas('LISTA DE TAREFAS')
sleep(1)
resposta = 0
while True:
    menu()
    resposta = leiaint('Sua escolha: ')
    sleep(0.6)
    if resposta == 5:
        sleep(0.5)
        tarefas('FINALIZANDO O PROGRAMA')
        sleep(1)
        break
    task(resposta)

