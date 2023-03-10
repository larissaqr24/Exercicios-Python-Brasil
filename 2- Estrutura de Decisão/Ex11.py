'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''

salario_colaborador = int(input('Qual é o seu salário: '))
print(f'Salário antes do reajuste : {salario_colaborador}')
if salario_colaborador <= 280:
    aumento = (280 * 20)/ 100
    print('Aumento de 20%')
    print(f'Aumento de {aumento} reais.')
    novo_salario = salario_colaborador + aumento
    print(f'Salário novo é de: {novo_salario}')
elif salario_colaborador > 280 and salario_colaborador <= 700:
    aumento = ( 280 * 15)/100 and (700 * 15)/100
    print('Aumento de 15%')
    print(f'Aumento de {aumento} reais.')
    novo_salario = salario_colaborador + aumento
    print(f'Salário novo é de: {novo_salario}')
elif salario_colaborador > 700 and salario_colaborador <= 1500:
    aumento = (700 * 10)/100 and (1500 * 10)/100
    print('Aumento de 5%')
    print(f'Aumento de {aumento} reais.')
    novo_salario = salario_colaborador + aumento
    print(f'Salário novo é de: {novo_salario}')
elif salario_colaborador > 1500:
    aumento = (1500 * 5)/100
    print('Aumento de 5%')
    print(f'Aumento de {aumento} reais.')
    novo_salario = salario_colaborador + aumento
    print(f'Salário novo é de: {novo_salario}')
