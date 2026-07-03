#CONDIÇÕES
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.2}'.format(m))
if m >= 5.0:
    print('Parabéns você passou de ano')
else:
    print('Infelizmente você reprovou nessa disciplina')
