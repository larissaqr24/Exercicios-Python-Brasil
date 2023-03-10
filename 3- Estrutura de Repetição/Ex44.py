'''Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. 
Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. 
Para finalizar o conjunto de votos tem-se o valor zero'''

print('*****Candidatos para Eleição Presidencial*****')
print('1 - Jose')
print('2 - João')
print('3 - Lucas')
print('4 - Marcio')
print('5 - Voto Nulo')
print('6 - Voto em Branco')

voto_jose = 0
voto_joao = 0
voto_lucas = 0
voto_marcio = 0
voto_nulo = 0
voto_branco = 0
votos = float(input('Digite seu voto de acordo com a tabela: '))

while True:
    if votos == 1:
        voto_jose += 1
        votos = int(input('Digite seu voto de acordo com a tabela: '))
    elif votos == 2:
        voto_joao += 1
        votos = int(input('Digite seu voto de acordo com a tabela: '))
    elif votos == 3:
        voto_lucas += 1
        votos = int(input('Digite seu voto de acordo com a tabela: '))
    elif votos == 4:
        voto_marcio +=1
        votos = int(input('Digite seu voto de acordo com a tabela: '))
    elif votos == 5:
        voto_nulo +=1
        votos = int(input('Digite seu voto de acordo com a tabela: '))
    elif votos == 6:
        voto_branco += 1
        votos = int(input('Digite seu voto de acordo com a tabela: '))
    else:
        votos < -1 and votos > 6
        print('Código inválido.')
        break

perc_nulo = (voto_nulo * votos) / 100
perc_branco = (voto_branco * votos) / 100

print(f'Total de votos do José: {voto_jose}')
print(f'Total de votos do João: { voto_joao}')
print(f'Total de votos do Lucas: { voto_lucas}')
print(f'Total de votos do Marcio: { voto_marcio}')
print(f'Total de votos nulo: {voto_nulo}')
print(f'Total de votos em branco: {voto_branco}')
print(f'A porcentagem de votos nulos sobre o total de votos é: {perc_nulo}%')
print(f'A percentagem de votos em branco sobre o total de votos é: {perc_branco}%') 
