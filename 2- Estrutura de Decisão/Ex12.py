'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
 O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.'''

valor_hora = int(input('Quanto você ganha por hora: '))
horas_trabalhadas = int(input('Quantas horas você trabalha no mês: '))
salario_bruto = valor_hora * horas_trabalhadas
print(f'Salário bruto é: {salario_bruto}')
if salario_bruto <= 900:
    perc_ir = 0
    perc_fgts = 0
    perc_inss = 0
    print('Isento de desconto.')
elif salario_bruto <= 1500:
    perc_ir = 5
    desconto_ir = (salario_bruto*perc_ir)/100
    perc_inss = 10
    inss = (salario_bruto*perc_inss) /100
    perc_fgts = 11
    fgts = (salario_bruto*perc_fgts)/100
    # sindicato = (salario_bruto)
elif salario_bruto <= 2500:
    perc_ir = 10
    desconto_ir = (salario_bruto*perc_ir)/100
    perc_inss = 10
    inss = (salario_bruto*perc_inss) /100
    perc_fgts = 11
    fgts = (salario_bruto*perc_fgts)/100
elif salario_bruto > 2500:
    perc_ir = 20
    desconto_ir =(salario_bruto*perc_ir)/100
    perc_inss = 10
    inss = (salario_bruto*perc_inss) /100
    perc_fgts = 11
    fgts = (salario_bruto*perc_fgts)/100
total_desconto = inss + desconto_ir
salario_liquido = salario_bruto - total_desconto

print(f'''Salário Bruto: ({valor_hora} * {horas_trabalhadas})        : R$ {salario_bruto}
(-) IR ({perc_ir}%)                     : R$  {desconto_ir}
(-) INSS ({perc_inss}%)                 : R$  {inss}
FGTS ({perc_fgts}%)                      : R$  {fgts}
Total de descontos              : R$  {total_desconto}
Salário Liquido                 : R$  {salario_liquido}''')
