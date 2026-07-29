#Operadores aritméticos dentro do python
#Adição '+'
#Subtração '-'
#Multiplicação '*'
#Divisão '/'
#Potenciação '**'

#Divisão inteira '//'
#Resto da Divisão ou Módulo '%'

#Para saber o resultado de uma operação matemática, será necessário utilizar 2 simbolos de 'igual'
#Dessa forma : '==', apenas 1 'igual/=' é atribuição, e lemos ele como 'recebe'

#Ordem de precedência:
#1ª Coisa calculada são os "()"
#2ª Coisa calculada são as "**" (potências)
#3ª Coisa calculada sequenciamente em ordem de expressão : "*, /, //, %",
#Independente se existem várias operações no mesmo, vai ser realizada da esquerda para a direita obrigatóriamente na ordem da expressão.
#4ª Coisa calculada, são "+ , -"

nome=input('Digite seu nome: ')
print('Prazer em te conhecer {:=^20}!'.format(nome))

#O nome disso é alinhamento. O ":" funciona como espaços
#O sinal de '>' alinha com extrema direita
#O sinal de '<' alinha com extrema esquerda
#O sinal de '^' alinha com o centro
#O '20' é a quantidadade de espaços
#O sinal de '=' também funciona para qualquer coisa que possa ser utilizado. como o underline.
