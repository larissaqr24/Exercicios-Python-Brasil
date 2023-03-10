'''Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, 
o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos 
duas funções: uma para fazer a conversão e uma para a saída.
Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. 
Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. 
Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as 
vezes que desejar.'''

import datetime

hora = input('Informe a hora: ')
def converte_hora(hora):
    hora_convertida = datetime.datetime.strptime(hora,"%H:%M")
    hora_convertida = datetime.datetime.strftime(hora_convertida,"%I:%M %p")
    return hora_convertida 

while True:
    cont = input('Deseja cotinuar? ')
    if cont == ('sim'):
        hora = input('Informe a hora: ')
    else:
        print('Obrigado! Até mais.')
        break

print(converte_hora(hora))