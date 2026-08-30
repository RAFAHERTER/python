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
afazeres = list()

def tarefas(msg):
    tamanho = len(msg) + 8
    print('-'*tamanho)
    print(f'{msg.center(tamanho)} ')
    print('-'*tamanho)

def leiaint(msg):
    msg = str(msg)
    if msg.isnumeric():
        return int(msg)
    else:
        while True:
            print('ERRO!! Digite apenas números inteiros: ')


def menu():
    print('-'*70)
    print("""    [ 1 ] - Adicionar tarefa
    [ 2 ] - Listar tarefa
    [ 3 ] - Marcar tarefa como concluída
    [ 4 ] - Remover tarefa
    [ 5 ] - Ver estatísticas
    [ 6 ] - Sair  """)
    print('-'*70)

def listar_tarefas():
    sleep(1)
    if len(afazeres) == 0:
        print('LISTA VAZIA. POR FAVOR COLOCAR UMA TAREFA!')
    else:
        for pos, c in enumerate(afazeres):
            print(f'{pos + 1}° TAREFA : ', end='')
            print(f'{c['Descrição']} - Prioridade {c['Prioridade']} - Situação {c['Situação']}')
            print()

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
        listar_tarefas()
        concluido = leiaint(input('Qual tarefa foi realizada? [APENAS NÚMEROS] ')) - 1
        while concluido >= len(afazeres):
            print('ERRO!! Número incompatível com a quantidade de TAREFAS')
            print('POR FAVOR TENTE NOVAMENTE!!')
            concluido = leiaint(input('Qual tarefa foi realizada? [APENAS NÚMEROS] '))
        afazeres[concluido]['Situação'] = 'Concluído'
        print('Tarefa marcada como "CONCLUÍDA"')
        sleep(0.6)

    if num == 4:
        tarefas('REMOVENDO TAREFAS')
        listar_tarefas()
        print('-'*70)
        escolha = leiaint(input('Qual tarefa deseja remover? [Apenas números] '))
        del afazeres[escolha - 1]
        print('REMOVENDO TAREFA')
        sleep(1)
        tarefas('TAREFA REMOVIDA COM SUCESSO')
    return afazeres

tarefas('LISTA DE TAREFAS')
sleep(1)
resposta = 0
while True:
    menu()
    resposta = int(input('Sua escolha: '))
    if resposta == 6:
        sleep(0.5)
        tarefas('FINALIZANDO O PROGRAMA')
        sleep(1)
        break
    task(resposta)

