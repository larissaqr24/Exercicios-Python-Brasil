'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''

area_pintada = float(input('Tamanho em metros quadrados da área a ser pintada: '))

# 1 litro para 3 metros quadrados 
# 18 litros 80 reais
lata = 18 * 3
if area_pintada <= lata:
    print('Quantidades de latas: 1')
elif area_pintada >= lata:
    print(f'Quantidades de latas:  {round((area_pintada/lata))}')
quantidade_de_lata = round((area_pintada/lata))
valor = 80 * quantidade_de_lata
print(f'{valor} reais')
    
