print('Conversor de segundos para Horas, minutos e segundos')
tot_segundo = int(input('Quantos segundos? '))
horas_inteira = tot_segundo // 3600
minutos = tot_segundo // 60
segundos = 0
if horas_inteira >= 1:
    resto = tot_segundo % 3600
    minutos = resto // 60
if minutos >= 1:
    resto = tot_segundo % 60
    segundos = resto // 1
if horas_inteira == 0 and minutos == 0:
    segundos = tot_segundo
print('{} segundos = {} hora(s), {} minuto(s) e {} segundo(s)'.format(tot_segundo, horas_inteira, minutos, segundos))
