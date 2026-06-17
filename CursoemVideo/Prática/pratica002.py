n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s=n1+n2
sub=n1-n2
m=n1*n2
d=n1/n2
din=n1//n2
pot=n1**n2

print('A soma vale {}, a subtração vale {}, a multiplicação é {}, \n'
      'a divisão vale {:.3}, a divisão inteira vale {} \n'
      'e a potência entre eles é {}'.format(s, sub, m,d,din, pot))
#para pular linha no python basta colocar um '\n'. E para manter na mesma linha
#no entre dois prints diferentes, basta coloca um ', end=' ' '