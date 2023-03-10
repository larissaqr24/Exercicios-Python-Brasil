'''Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, 
o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar 
com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa).
 Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema.
  Após todos os alunos terem respondido informar:
Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.
Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
Após concluir isto você poderia incrementar o programa 
permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.'''

maior_nota_aluno = ''
menor_nota_aluno = ''

total_alunos = 0
media = 0.0
nota_geral = 0.0

while True:
    nota_aluno = 0.0

    nome = input('Deseja informar o nome de aluno? SIM OU NAO :').upper()
    if  nome == 'SIM':
        nome_aluno = input('Infome o nome do aluno: ').upper()
        primeira_nota = input('Informe sua nota referente a Questão 1: ')
        segunda_nota = input('Informe sua nota referente a Questão 2: ')
        terceira_nota = input('Informe sua nota referente a Questão 3: ')
        quarta_nota= input('Informe sua nota referente a Questão 4: ')
        quinta_nota = input('Informe sua nota referente a Questão 5: ')
        sexta_nota = input('Informe sua nota referente a Questão 6: ')
        setima_nota = input('Informe sua nota referente a Questão 7: ')
        oitava_nota = input('Informe sua nota referente a Questão 8: ')
        nona_nota = input('Informe sua nota referente a Questão 9: ')
        decima_nota= input('Informe sua nota referente a Questão 10: ')
    elif nome == 'NAO':
        print('Sistema encerrado.')
        break

    if primeira_nota == 'A':
        nota_aluno += 1
        print('Resposta Correta.')
    else:
        print('Resposta errada.')

    if segunda_nota == 'B':
        nota_aluno += 1
        print('Resposta Correta.')
    else:
        print('Resposta errada.') 

    if terceira_nota == 'C':
        nota_aluno += 1
        print('Resposta Correta.')
    else:
        print('Resposta errada.') 
    if quarta_nota == 'D':
        nota_aluno += 1
        print('Resposta Correta.')
    else:
        print('Resposta errada.')

    if quinta_nota == 'E':
        nota_aluno += 1
        print('Resposta Correta.')
    else:
        print('Resposta errada.') 

    if sexta_nota == 'E':
        nota_aluno += 1
        print('Resposta Correta.')
    else:
        print('Resposta errada.') 
    if setima_nota == 'D':
        nota_aluno += 1
        print('Resposta Correta.')
    else:
        print('Resposta errada.') 

    if oitava_nota == 'C':
        nota_aluno += 1
        print('Resposta Correta.')
    else:
        print('Resposta errada.') 

    if nona_nota == 'B':
        nota_aluno += 1
        print('Resposta Correta.')
    else:
        print('Resposta errada.') 

    if decima_nota == 'A':
        nota_aluno += 1
        print('Resposta Correta.')
    else:
        print('Resposta errada.')


    total_alunos += 1
    nota_geral += nota_aluno

    if maior_nota_aluno == '':
        maior_nota = nota_aluno
        maior_nota_aluno = nome_aluno

        menor_nota_aluno = nome_aluno
        menor_nota = nota_aluno
    else:
        if nota_aluno > maior_nota:
            maior_nota = nota_aluno
            maior_nota_aluno = nome_aluno
        elif nota_aluno < menor_nota:
            menor_nota = nota_aluno
            menor_nota_aluno = nome_aluno
            


media = nota_geral / total_alunos

print(f'Total de alunos: {total_alunos}')
print(f'Média: {media}')
print(f'Maior nota - Aluno: {maior_nota_aluno} - Nota: {maior_nota}')
print(f'Menor nota - Aluno: {menor_nota_aluno} - Nota: {menor_nota}')
