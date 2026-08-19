'''
Funções PARTE 2

Tópicos abordados nessa aula:

 - Interactive Help;
 - docstrings;
 - Argumentos opcionais;
 - Escopo de Variáveis;
 - Retorno de resultados.

1) Interactive Help

Entre no python console e digite 'help()'
Nele você pode digitar os comandos que podemos usar no python
E retornará como um manual de como pode usar diversas outras
funcionalidades para o comando digitado.

Ou, Você pode acessar através do próprio editor de
código, vulgo neste mesmo local, digitando:
'help("comando que deseja estudar o manual")'

Ou, é possível também, imprimir na tela o suporte
iterativo através do comando print("comando que
deseja estudar".__doc__)
Porém aparentemente não está retornando alguns comandos.


2) DOCSTRINGS

String de documentação

def contador(i, f, p): Esses parâmetros podem ser óbvios
apenas para quem está os codificando, quem está
lendo o código precisa de uma

    c = i
    while c<= f :
    print(f'{c}', end=' ')
        c += p
    print('FIM')

contador (2, 10, 2) Para o leitor, esses números não estão
claros sobre representam, pra isso é necessário as DOCSTRINGS.
Elas funcionam como um manual da função que você criou,
informando o que cada variável representa, o que cada parâmetro
representa e tudo que estiver dentro de uma função.

Para fazer isso é muito simples:
Basta abrir aspas duplas 3 vezes logo abaixo do comando 'def'

#

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela:
    :parâmetro i: Início da contagem
    :parâmetro f: Fim da contagem
    :parâmetro p: Passo da contagem
    :return: Sem retorno
    """
    c = i
    while c<= f :
        print(f'{c}', end=' ')
        c += p
        print('FIM')
help(contador) #Apenas desse jeito, é impossível saber o que os parâmetros representam.
#

#PARÂMETROS OPCIONAIS.

def somar(a, b, c = 0): SE por acaso o um dos parâmetros não
            receber valor, ele irá ignorar o parâmetro
            e substituir o valor por 0
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4) - Nesse caso, como não tem o terceiro parâmetro,
        iria dar erro se não tivesse o 'c=0' nos parâmetros.
        Isso torno o terceiro parâmetro opcional para a função
#
def somar(a=0, b=0, c = 0): #Também posso fazer para todos
    """
        -> Soma todos os valores e mostra o resultado na tela
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    :return: sem retorno
    """
    s = a + b + c
    print(f'A soma vale {s}')

somar(3,2, 5)
somar(8, 4)
somar()
#
'''

