'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.'''

valor_hora = float(input('Quanto você ganha por hora? '))
valor_horas_trabalhadas_no_mes = float(input('Quantas horas por mês? '))
print(f'{valor_hora * valor_horas_trabalhadas_no_mes}')