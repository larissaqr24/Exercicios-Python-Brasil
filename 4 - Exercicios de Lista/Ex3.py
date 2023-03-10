'''Faça um Programa que leia 4 notas, mostre as notas e a média na tela.'''

lista = []

for x in range(4):
    notas = float(input('Digite sua nota: '))
    lista.append(notas)
print(lista)
print(f'A média da nota é: {round(sum(lista) / 4,2)}')

