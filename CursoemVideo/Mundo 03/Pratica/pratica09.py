times = ('Flamengo', 'Palmeiras', 'Flamengo', 'Corinthians', 'Palmeiras', 'Flamengo', 'São Paulo')
insira = input('Digite o nome de um time: ').strip().title()
if insira in times:
    print(f'O time {insira} aparece {times.count(insira)} vezes')
else:
    print(f'O time {insira} não aparece nenhuma vez')

