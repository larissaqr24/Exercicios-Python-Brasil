'''Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.'''

temp_c = float(input('Informe uma temperatura em ºC: '))
temp_f = float(temp_c * 9/5 + 32)
print(temp_f)