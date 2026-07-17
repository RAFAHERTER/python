primeiro = int(input('Primeiro termo: '))
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