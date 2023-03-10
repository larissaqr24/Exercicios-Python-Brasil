'''Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
'''

from datetime import date, datetime
dt = input('Informe uma data: ')
data= datetime.strptime(dt, '%d/%m/%Y').date()
print(data)

dataFormatada = data.strftime('%d/%m/%Y')
print(dataFormatada)