'''Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
Dica: utilize uma função de arredondamento.'''

num = float(input('Informe um número: '))
if num == round(num):
    print('Número é inteiro')
else:
    print('Número é decimal')