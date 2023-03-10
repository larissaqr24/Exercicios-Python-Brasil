'''Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida.'''

idade = []
altura = []
nomes = []
for x in range(5):
    nome = input('Informe seu nome: ')
    nomes.append(nome)
    for i in range(1):
        id = int(input('Informe sua idade: '))
        idade.append(id)
        al = float(input('Informe sua altura: '))
        altura.append(al)

id_novalista = idade[:: -1]
print(f'Idade: {id_novalista}')
alt_novalista = altura[:: -1]
print(f'Altura: {id_novalista}')
