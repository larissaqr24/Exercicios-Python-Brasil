'''Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor 
do saque e depois informar quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de
600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.'''

saque = int(input('Qual o valor do saque? '))
n1 = 0
n5= 0
n10= 0
n50 =0
n100= 0
restante = saque
if saque >= 10 and saque <= 600:

    while restante > 0:
        if restante >= 100:
            restante = restante - 100
            n100 += 1
        elif restante >= 50:
            restante = restante - 50
            n50 += 1
        elif restante >= 10:
            restante = restante - 10
            n10 += 1
        elif restante >= 5:
            restante = restante - 5
            n5 += 1
        elif restante  >= 1:
            restante = restante - 1
            n1 += 1
    print(f'Você vai precisar de {n100} notas de cédula 100')
    print(f'Você vai precisar de {n50} notas de cédula 50')
    print(f'Você vai precisar de {n10} notas de cédula 10')
    print(f'Você vai precisar de {n5} notas de cédula 5')
    print(f'Você vai precisar de {n1} notas de cédula 1')        
else:
    print('O saque tem que ser entre 10 a 600 reais.')



