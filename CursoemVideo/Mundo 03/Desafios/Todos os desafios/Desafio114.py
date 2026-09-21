'''Crie um código em python que teste se o site pudim está acessível pelo 
computador do usuário.
'''
#Sozinho
import requests
url = 'http://www.pudim.com.br'

try:
    response = requests.get(url, timeout= 5)
    if response.status_code == 200:
        print('O site está acessível!')
    else:
        print('O site não está acessível. Código de status:', response.status_code)
except:
    print('O site não está acessível. Ocorreu um erro ao tentar acessar o site.')

