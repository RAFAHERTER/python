'''primeiro = int(input('Primeiro termo: '))
razao = int(input('Insira a razao: '))
qtt_termo = 0
termo = 0
while qtt_termo != 10:
    qtt_termo = qtt_termo + 1
    termo = primeiro + (qtt_termo -1) * razao
    print('{} '.format(termo), end='')
mais_termo = int(input('\nGostaria de ver por mais quantos termos? '))
alvo = mais_termo + qtt_termo
if mais_termo != 0:
    while qtt_termo != alvo:
        qtt_termo = qtt_termo + 1
        termo = primeiro + (qtt_termo - 1) * razao
        print('{} '.format(termo), end='')
else:
    print('Programa finalizado com sucesso!')

    #Refazendo sozinho (DEU CERTO)
print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
contador = 1
termo = primeiro
mais_termo = 1

while contador <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    contador += 1
print('PAUSA')
while  mais_termo > 0:
    mais_termo = int(input('Quantos termo você quer mostrar a mais? '))
    if mais_termo > 0:
        for c in range(10, 10 + mais_termo):
            termo += razao
            contador += 1
            print('{} -> '.format(termo), end='')
        print('PAUSA')
    elif mais_termo == 0:
        print('Progressão finalizada com {} termos mostrados'.format(contador))
print('FIM')

'''
#Fazendo com o GB
print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
