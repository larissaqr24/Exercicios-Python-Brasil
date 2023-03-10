'''Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd'.'''

nome = input('Informe seu nome: ')
while True:
    if len(nome) > 3:
        print('Nome válido.')
        break
    else:
        print('Nome deve conter mais que 3 caractres.')
        nome = input('Informe seu nome: ')
    

idade = int(input('Informe sua idade: '))
while True:
    if idade >= 0 and idade <= 150:
        print('Idade válida.')
        break
    else:
        print('Idade inválida.')
        idade = int(input('Informe sua idade: '))

salario = float(input('Informe seu sálario: '))
while True:
    if salario > 0:
        print('Saláro válido')
        break
    else:
        print('Salário inválido.')
        salario = float(input('Informe seu sálario: '))

sexo = input('Informe seu Sexo: ').upper()
while True:
    if sexo == 'F' or sexo == 'M':
        print('Sexo válido')
        break
    else:
        print('Sexo inválido')
        sexo = input('Informe seu Sexo: ').upper()

estado_civil = input('Informe seu estado civil: ').upper()
while True:
    if estado_civil == 'S' or estado_civil == 'C' or estado_civil == 'V' or estado_civil == 'D':
        print('Estado Civil válido.')
        break
    else:
        print('Estado Civil inválido.')
        estado_civil = input('Informe seu estado civil: ').upper()

