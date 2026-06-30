#------- FASE 9 -------
'''
        Manipulação de TEXTOS
                TEORIA

Toda String e/ou cadeia de caracteres, para o python,
estará compreendido entre aspas simples ou aspas duplas.

Nesta aula vamos aprender modos de manipular essa cadeia de caratceres
para que podemos ter funcionalidades específicas e que vão nos ajudar a resolver problemas futuros.

É possível fazer fatiamento de string.
Temos um exemplo "Olá, Mundo!"
temos 11 caracteres
caso seja mandado printar [caracter qualquer, ele vai mostrar apenas o caracter naquela posição]
Use o exemplo abaixo.
Obs: O número 1 não é o primeiro caractere e sim o "0"(zero)

'''
#------- FATIAMENTO DE STRING -------
#Da esquerda para direita representa: Início, final, repetições de X em X.
frase='Curso em Vídeo python'
print(frase[9:21:2]) #Vou começar no caractere 9, vou parar no 21 e vou pular de 2 em 2
print(frase[:5]) #Vou até o quinto caractere
print(frase[15:]) #Vou começar do 15 caractere e vou até o final
print(frase[9::3]) #Vou começar a partir do 9, ir até o final, e mostrar as letras de 3 em 3

#------- ANÁLISE DE STRING -------
# Lembre-se que dentro do python, no fatiamento o último valor é sempre ignorado!!
print(len(frase)) #Serve para medir a quantidade de caracteres dentro de uma string

print(frase.count('o',0,14)) #Serve para contar a quantidade de letras 'o'(minúsculas) dentro da frase, ja com o fatiamento embutido.

print(frase.find('deo')) #(Eu encontrei'deo' na posição '11') Irá me mostrar onde começou o 'deo' que foi a partir do caractere 11.

print(frase.find('Android'))#Quando receber uma posição -1, significa que string 'Android' não existe dentro de 'frase'.

print('Curso' in frase) #Ele mostra se existe ou não 'Curso', dentro de 'frase' com 'true' ou 'false'

#------- TRANSFORMAÇÃO DE STRING -------

print(frase.replace('python','Android'))#Substituí uma palavra dentro da variável por outra.
print(frase.upper())#Transforma a frase toda em letras maiúsculas.
print(frase.lower())#Transforma a frase toda em letras minúsculas.
print(frase.capitalize())#Transformar toda a frase e deixar em minúsculo, porém só o primeiro carácter deixará em maiúsculo.
print(frase.title())#Deixa os primeiros dígitos de todas as palavras em maiúsculo, e o restante das letras minúsculo.

learn= '   Aprenda Python  ' #Note que existem vários caracteres com espaços, e para remover esses espaços inúteis...
print(len(learn))
print(len(learn.strip()))
print(learn.strip()) #Podemos remover os espaços inúteis dentro da string (tanto no começo, como no final).
print(learn.rstrip())#Remove apenas os espaços inúteis da direita
print(learn.lstrip()) #Remove apenas os espaços inúteis da esquerda

#------- DIVISÃO DE STRING -------

print(frase.split()) #Vai fazer uma divisão entre os espaços que existe dentro da string e separá-los.
#O 'split' vai divir uma string em uma lista, onde cada palavra será separado através do espaço

#------- JUNÇÃO DE STRING -------

print('-'.join(frase)) #antiburro

#Obs: Uma string é IMUTÁVEL, isto é, não é possível mudar ela, a não ser que seja realizado uma função de transformação
#nela e também faça uma atribuição nela.


