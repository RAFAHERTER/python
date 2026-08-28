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


def menu():
    print('-'*30)
    print("""    [ 1 ] - Adicionar tarefa
    [ 2 ] - Listar tarefa
    [ 3 ] - Marcar tarefa como concluída
    [ 4 ] - Remover tarefa
    [ 5 ] - Ver estatísticas
    [ 6 ] - Sair  """)
    print('-'*30)

def task(num):
    global afazeres
    descricao = dict()
    if num == 1:
        descricao['Descrição'] = str(input('Descrição da Tarefa: '))
        descricao['Prioridade'] = str(input('Prioridade da Tarefa: '))
        afazeres.append(descricao.copy())
        descricao.clear()
    if num == 2:
        tarefas('LISTANDO AS TAREFAS')
        sleep(1)
        if len(afazeres) == 0:
            print('LISTA VAZIA. POR FAVOR COLOCAR UMA TAREFA!')
        else:
            for pos, c in enumerate(afazeres):
                print(f'{pos + 1}° TAREFA : ', end = '')
                print(f'{c['Descrição']} - Prioridade {c['Prioridade']}')
                print()

    return afazeres

tarefas('LISTA DE TAREFAS')
sleep(1)
while True:
    menu()
    resposta = int(input('Sua escolha: '))
    if resposta == 6:
        sleep(0.5)
        tarefas('FINALIZANDO O PROGRAMA')
        sleep(1)
        break
    task(resposta)

