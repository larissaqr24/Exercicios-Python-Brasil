'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
Média de Aproveitamento  Conceito
Entre 9.0 e 10.0        A
Entre 7.5 e 9.0         B
Entre 6.0 e 7.5         C
Entre 4.0 e 6.0         D
Entre 4.0 e zero        E'''

primeira_nota = float(input('Qual é sua nota: '))
segunda_nota = float(input('Qual é sua nota: '))
media = (primeira_nota + segunda_nota) /2
print(f'Média da nota: {media}')
if media == 10 or media >= 9:
    print('NOTA A')
elif media >= 7.5 and media < 9:
    print('NOTA B')
elif media >= 6 and media < 7.5:
    print('NOTA C')
elif media >= 4 and media < 6:
    print('NOTA D')
else:
    print('NOTA E')