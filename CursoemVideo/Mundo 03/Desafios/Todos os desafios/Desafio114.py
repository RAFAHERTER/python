'''Crie um código em python que teste se o site pudim está acessível pelo 
computador do usuário.
'''
#Sozinho
import requests
url = 'http://www.pudim.com.br'

try:
    response = requests.get(url, timeout= (3, 10)) #O timeout pode ser separado entre ("Tempo de conectar", "Tempo para receber a resposta/dados") 
    if response.status_code == 200:
#O código 200 representa um "Tudo OK"
#Códigos começados por 2 é de sucesso
#Códigos começados por 3 redirecionamento - site mandou você para outro lugar
#Códigos começados por 4 ERRO do cliente / Usuário
#Códigos começados por 5 ERRO do servidor

        print('O site está acessível!')
    else:
        print('O site não está acessível. Código de status:', response.status_code)
except:

    print('O site não está acessível. Ocorreu um erro ao tentar acessar o site.')

