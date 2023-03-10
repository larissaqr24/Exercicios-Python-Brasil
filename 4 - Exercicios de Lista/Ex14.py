'''Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a 
participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".'''



lista =['Telefonou para a vítima?',
        'Esteve no local do crime?',
        'Mora perto da vítima? ',
        'Devia para a vítima?',
        'Já trabalhou com a vítima?']

resposta = 0

for x in lista: 
    print(x)
    resultado = input('Resposta Sim ou Não: ')
    if resultado == 'sim':
        resposta += 1 

if resposta == 2 :
    print("Suspeita")
elif resposta == 3 or resposta == 4:
    print("Cúmplice")
elif resposta == 5:
    print("Assassino")
else: 
    print("Inocente")

