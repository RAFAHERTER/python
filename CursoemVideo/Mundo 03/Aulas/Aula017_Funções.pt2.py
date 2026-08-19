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

#ESCOPO DE VARIÁVEIS

Escopos de declarações

"Basicamente na programação, escopo é o local onde uma variável
vai existir e o local onde a variável não vai mais existir."

#

def teste():
    Caso eu faça, por exemplo
    n = 6 Ele irá criar uma nova variável 'n' com um valor diferente
    Porém, a variável do programa principal não será alterada.
    x = 8 A variável 'x' Só irá funcionar dentro da função
    isso é chamado de escopo local
    print(f'Na função teste, n vale {n}')
    Por outro lado, a variável 'n' vai funcionar para todo o programa
    Dependendo, obviamente do local de onde está criando a função.
    print(f'Na função teste, x vale {x}')



#Programa principal
n = 2 Quando eu tenho uma variável no programa principal
Ela é chamada de variável global
print(f'No programa principal, n vale {n}')
teste()

#

def teste(b):
    global a #Quando eu faço isso, estou dizendo para usar estritamente a variável 'a' no programa principal
    a = 8 #E assim o 'a' do programa principal irá ser alterado também.
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

#Programa Principal
a = 5
teste(a)
print(f'A fora vale {a}')

#

#Retorno de VALORES
#Usa-se o comando return
def somar(a=0, b=0, c = 0):
    s = a + b + c
    return s #Funções que irão retornar resultados, são muito
        #Úteis quando eu quero ter personalização dos resultados
        #E também poder mexer nas variáveis dentro do programa principal
r1 = somar(3,2,5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Os resultados foram {r1}, {r2}, {r3}')

#Pratica

def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f #funciona para valores booleanos

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2}, {f3}')

'''
def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False
num = int(input('Digite um número: '))
if par(num): #Sub entende-se que, caso o valor retornado de 'par(num)' seja True
    print('É par')
#print(par(num))
else:
    print('Não é par')


