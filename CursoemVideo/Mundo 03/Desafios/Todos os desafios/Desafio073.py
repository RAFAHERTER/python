'''times = ('Palmeiras', 'Flamengo', 'Athletico Paranaense', 'Fluminense', 'Red Bull Bragantino', 'Bahia', 'Corinthians', 'Cruzeiro',
         'Botafogo', 'Coritiba', 'Vitória', 'São Paulo', 'Atlético Mineiro', 'Santos', 'Internacional',
         'Grêmio', 'Vasco da Gama', 'Mirassol', 'Remo', 'Chapecoense')
chapecoense = times.index('Chapecoense') + 1
print(f'Lista dos nomes dos atletas em ordem alfebética: {sorted(times)}')
print(f'Os 5 primeiros colocados são: {times[:5]}')
print(f'Os 4 últimos são {times[-4:]}')
print(f'O Chapecoense está na posição {chapecoense}')
'''
#Com GB
print('-='*15)

times = ('Palmeiras', 'Flamengo', 'Athletico Paranaense', 'Fluminense', 'Red Bull Bragantino', 'Bahia', 'Corinthians', 'Cruzeiro',
         'Botafogo', 'Coritiba', 'Vitória', 'São Paulo', 'Atlético Mineiro', 'Santos', 'Internacional',
         'Grêmio', 'Vasco da Gama', 'Mirassol', 'Remo', 'Chapecoense')
print(f'Lista de time do Brasileirão: {times}')
print('-='*15)
print(f'Os 5 primeiros são: {times[:5]}') #Letra A
print('-='*15)
print(f'Os 4 últimos colocados são: {times[-4:]}') #Letra B
print('-='*15)
print(f'Time em ordem alfabética: {sorted(times)}') #Letra C
print('-='*15)
print(f'O Chapecoense está na posição {times.index("Chapecoense")+1}') #Letra D

