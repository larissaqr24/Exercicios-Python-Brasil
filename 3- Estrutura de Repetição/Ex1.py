'''Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.'''

nota = int(input('Informe uma nota, entre 0 e 10: '))
while True:
    if nota >= 0 and nota <=10:
        print('Valor Válido')
        break
    else:
        print('Valor inválido')
        nota = int(input('Informe uma nota, entre 0 e 10: '))