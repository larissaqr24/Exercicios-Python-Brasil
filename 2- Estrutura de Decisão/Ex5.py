'''Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;#  "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.'''

primeira_nota = float(input('Digite sua nota: '))
segunda_nota = float(input('Digite sua nota: '))
media = (primeira_nota + segunda_nota) /2 
print(f'Sua média é: {media}')

if media == 10:
    print('Aprovado com distinção')
elif media >= 7:
    print('Aprovado')
elif media < 7:
    print('Reprovado')
