'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar; positivo ou negativo; inteiro ou decimal.'''

num1= float(input('Informe um número: '))
num2= float(input('Informe outro número: '))
print('Letra A: O número é par ou impar')
print('Letra B: O número é positivo ou negativo')
print('Letra C: O número é inteiro ou decimal')
opcao = input('Qual operação deseja realizar?').upper()

if opcao == 'A':
    if (num1 % 2 == 0):
        print(f'O número {num1} é par')
    else:
        print(f'O numero {num1} é impar')
    
    if (num2 % 2 == 0):
        print(f'O número {num2} é par')
    else:
        print(f'O numero {num2} é impar')

if opcao == 'B':
    if(num1 >= 0):
        print(f'O número {num1} é positivo')
    else:
        print(f'O número {num1} é Negativo')

    if(num2 >= 0):
        print(f'O número {num2} é positivo')
    else:
        print(f'O número {num2} é Negativo')
if opcao == 'C':
    if (num1 == round(num1)):
        print(f'O número {num1} é inteiro')
    else:
        print(f'O número {num1} é decimal')
        
    if (num2 == round(num2)):
        print(f'O número {num2} é inteiro')
    else:
        print(f'O número {num2} é decimal')