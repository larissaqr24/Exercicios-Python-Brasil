'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.'''

area_pintada = float(input('Tamanho em metros quadrados da área a ser pintada: '))
# 1 litro para 6 metros quadrados 
# 18 litros 80 reais
# 3,6 galões 25 reais
latas = 18 * 6 #108
galoes = 3.6 * 6 # 21,6
if area_pintada <= galoes:
    print('Quantidade de galoes:  1')
elif area_pintada <= latas:
    print('Quantidade de latas:  1')
else:
    


