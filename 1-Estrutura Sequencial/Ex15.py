'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.'''

salario_por_hora = float(input('Quanto você ganha por hora: '))
num_horas_trabalhadas_mes = float(input('Quantas horas trabalhadas por mês: '))
# imposto = 11%
# inss= 8%
# sindicato = 5%
salario_bruto = (salario_por_hora * num_horas_trabalhadas_mes)
print(f'Salário bruto é: {salario_bruto}')
imp_renda = (salario_bruto * 11) / 100 
print(f'Pago para o imposto de renda: {imp_renda}')
inss = (salario_bruto * 8) / 100
print(f'Pago para o inss: {inss}')
sindicato = (salario_bruto * 5) / 100
print(f'Pago para o sindicato: {sindicato}')
salario_liquido = (salario_bruto - imp_renda - inss - sindicato)
print(f'Salário liquído é: {salario_liquido}')