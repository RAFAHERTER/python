#Conversor de temperatura
fahrenheit = float(input('Digite uma temperatura em Fahrenheit: '))
celsius = (fahrenheit - 32) * (5 / 9)
print('A temperatura em {}° Fahrenheit é igual a {}° Celsius.'.format(fahrenheit, celsius))
