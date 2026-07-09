#------------- CORES NO TERMINAL --------------
""" Código ANSI para cores sempre irá começar com um contra-barra (\),
e logo em seguida, virá um código.
Sempre que quiser representar uma cor em python, representa-se com
"\033["código da cor" m]"

\033["style" "text" "background" m   #O 'm' fecha o código

Códigos para style (funcionam melhor, porém existem outros):
0, (none)
1, (bold)
3, (italic)
4,(underline)
7 (Negative)

Códigos para 'text':
30 branco
31 vermelho
32 verde
33 amarelo
34 azul
35 roxo - magenta
36 ciano
37 cinza - cor padrão
#caso queira usar mais cores, use uma biblioteca.

Códigos para 'back':
40 branco
41 vermelho
42 verde
43 amarelo
44 azul
45 roxo - magenta
46 ciano
47 cinza - cor padrão

Teste \033[0;30;41m
Teste \033[4;33;44m
Teste \033[1;35;43m
Teste \033[30;42m
Teste \033[m ---------#Fundo preto e letra cinza (mantém padrão do terminal)
Teste \033[7;30;m ---------#O '7' é um inversor, que inverte a cor branca. (fundo branco e letra preta)
"""

print('Teste')
