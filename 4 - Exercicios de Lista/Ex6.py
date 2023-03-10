'''Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, 
imprima o número de alunos com média maior ou igual a 7.0.'''


notas = []
nomes = []
for x in range(3):
    nome = input('Informe seu nome: ')
    nota_temp = []
    for n in range(4):
        nota_temp.append(float(input('Informe sua nota: ')))

    soma = sum(nota_temp)/ 4
    if soma >= 7:
        nomes.append(nome)
        notas.append(soma)
       

print('Lista dos aprovados!')
for x, nome in enumerate(nomes):
    print(f'Aluno: {nome} Nota: {notas[x]}')
