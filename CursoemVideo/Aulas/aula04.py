#Para fazer alguns códigos é necessário criar módulos
#Assim é necessário acessar bibliotecas

#Na linguagem da programação, é necessário realizar importações à essas bibliotecas

#A quantidade de comandos em python é limitada, justamente
#para evitar códigos extremamentes grandes.
#por isso é necessário realizar importações para que seja
#possível realizar outras funções.

#Para incluir algo em python, usamos o comando import.
#Isso irá resultar na importação de tudo que existe
#na biblioteca importada. (Mais generalista)

#Para incluir apenas um elemento da biblioteca,
#basta usar o from 'biblioteca' import 'elemento' , 'outro elemento' (mais específico)

#Na a biblioteca 'math' temos diversas funcionalidades
#que podem serem usadas, como:
#ceil - arredondamento pra cima
#floor - arredondamento pra baixo
#trunc - eliminar da ',' pra frente os números
#pow - potência
#sqrt - Raiz quadrada
#factorial
#Entre várias outras funcionalidades.

#Para ver qual são as bibliotecas disponíveis para
#serem acessadas, acesse o seguinte site:
#https://www.python.org/ - documentatin, python docs -
#library reference, E lá você terá várias funcionalidades
#dentro do pyhton.

import random
num= random.randint(0, 10)
print(num)
