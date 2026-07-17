print('----'*10)
print('10 termos de uma PA'.center(10))
print('----'*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Insira a razao: '))
qtt_termo = 0
termo = 0
while qtt_termo != 10:
    qtt_termo = qtt_termo + 1
    termo = primeiro + (qtt_termo -1) * razao
    print('{} '.format(termo), end='')
