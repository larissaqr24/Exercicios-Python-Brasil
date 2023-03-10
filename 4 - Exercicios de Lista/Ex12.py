'''Foram anotadas as idades e alturas de 30 alunos. 
Faça um Programa que determine quantos alunos com mais de 13 anos
possuem altura inferior à média de altura desses alunos.'''

idades = [12,13,13,15,16]
altura = [1.70,2.0,1.40,1.55,1.70]

media = sum(altura) / len(altura)
print(f'Média: {media}')

quantidades_alunos = 0
for i in range (len(idades)):
    if idades[i] >= 13 and altura[i] <= media:
        quantidades_alunos += 1 
print(f'O número de alunos com a altura inferior a média é: {quantidades_alunos}')

