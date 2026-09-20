'''
Enunciado:
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu
nome e idade em um arquivo de texto simples. O sistema só vai ter 2 opções:
Cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

Para arquivos, é utilizado algumas nomenclaturas em python 
para poder dar significado ao que será utilizado.

r : leitura
w: escrita (sobrescreve o conteúdo existente)
a: anexa ao final do arquivo
r+: leitura e escrita


from Desafio115.menu import sistema

        
''' 
#Também é possível mudar o diretório do terminal. O terminal encontra-se "parado" em relação ao arquivo. O necessário é usar o comando "cd" (change directory) no terminal e colocar o caminho correto que ele irá se alterar e isso poderá resolver o problema temporáriamente. Porém não é o ideal em termos de profissionalismo, tendo em vista que outra pessoa possa acessar o seu código e isso pode resultar em erro pois os diretórios não batem. Portanto o mais eficiente de se fazer é utilizando o método abaixo.

#O arquivo __file__ mostra exatamente o caminho completo feito para chegar no arquivo onde está

#A biblioteca "os" usará sua função para mudar o caminho retirando apenas o arquivo final. Restando apenas o local da mesma pasta.

#A função os.path.join junta um nome de arquivo 

import os
from Desafio115.menu import sistema

caminho_pasta = os.path.dirname(__file__)
caminho_arquivo = os.path.join(caminho_pasta, "texto.txt")


with open(caminho_arquivo, "w", encoding= "utf=8") as arquivo:
    conteudo = arquivo.write("Olá mundo!!") #O write retorna o conteudo como números, nesse caso retorna o números de caracteres que foi bem sucedido ao tentar colocar no arquivo
with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
    leitura = arquivo.read()
    print(leitura)



'''while True:
    escolha = sistema.opcoes()
    if escolha < 1 or escolha > 3:
        print('Escolha inválida!! Escolha novamente somente números entre 1 e 3')
    else:
        #if escolha == 1:

        #if escolha == 2:
            
        if escolha == 3:
            print(f'Saindo do programa!!')
            break
'''