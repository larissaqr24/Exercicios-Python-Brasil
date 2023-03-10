'''Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e 
devolva uma string no formato D de mesPorExtenso de AAAA.
 Opcionalmente, valide a data e retorne NULL caso a data seja inválida.'''

import datetime
import locale

data = input('Informe a data: ')
try:
    locale.setlocale(locale.LC_ALL,'pt_BR')
except Exception:
    locale.setlocale(locale.LC_ALL,'Portuguese_Brazil')
def converte_data(data):
    data = datetime.datetime.strptime(data,'%d/%m/%Y')
    data_convertida = datetime.datetime.strftime(data,'%d/%b/%Y')
    return data_convertida

print(converte_data(data))