'''Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
 Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, 
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).'''


temperatura = [25,27,23,18,15,18,16,23,14,28,25,20]
meses = ['Janeiro', 'Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
media_anual= sum(temperatura) /12
print(f'Média anual: {media_anual}')

print('Meses acima da média')
for x in range(12):
    if temperatura[x] >= media_anual:
        print(f'{meses[x]} - {temperatura[x]}°')


