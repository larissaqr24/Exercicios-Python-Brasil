'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da
 pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como
  "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado 
  como "Inocente".'''

print('Responda as perguntas abaixo, utilizando número 1 para SIM e 0 para NÃO:')
a = int(input('Telefonou para a vítima?' ))
b = int(input('Esteve no local do crime?' ))
c = int(input('Mora perto da vítima?' ))
d = int(input('Devia para a vítima?' ))
e = int(input('Já trabalhou com a vítima?' ))
soma = (a+b+c+d+e)
if soma == 2:
    print('Suspeita')
elif soma >=3 and soma <=4:
    print('Cúmplice')
elif soma == 5:
    print('Assasino')
else:
    print('Inocente')
