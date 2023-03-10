'''Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação 
de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e
passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este 
valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. 
Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar 
até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado,
exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. 
O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, 
cobrar o valor da prestação. 
Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.'''

def valorpagamento(valor_prestacao,dias_atraso):
    if dias_atraso == 0:
        return valor_prestacao
    elif dias_atraso != 0:
        multa = valor_prestacao * 3 / 100
        juros = dias_atraso * 0.1 /100
        return multa + valor_prestacao + juros
    

qtd_prestacao = 0
vl_total = 0.0

while True:
    valor_prestacao = float(input('Digite o valor da prestação: '))
    if valor_prestacao == 0:
        break

    dias_atraso = int(input('Informe a quantidade de dias em atraso: '))
    valor = valorpagamento(valor_prestacao,dias_atraso)
    qtd_prestacao += 1
    print(f'Valor da prestacao nº {qtd_prestacao} - R${round(valor,2)}')
    vl_total += valor
   

print('***** Relatório do Dia*****')
print(f'Total de prestações no dia: {qtd_prestacao}')
print(f'Total do valor no dia: R${round(vl_total,2)}')
