'''Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.'''

num = int(input('Informe um número: '))
if num >= 0:
    print('postivo')
elif num < 0:
    print('negativo')
else:
    print(f'{num} é neutro.')