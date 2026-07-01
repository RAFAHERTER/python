"""cidade= str(input('Digite o nome de sua cidade: ')).strip().title().capitalize().lower().upper()
print('Santo' in cidade.strip().title())"""
#Errado pois ele reconhece em toda a frase. No enunciado pedia apenas no começo.

#------------COM GUSTAVO GUANABARA-------------

cid= str(input('Qual cidade que você nasceu? ')).strip()
print(cid[0:5].upper() == 'SANTO')
