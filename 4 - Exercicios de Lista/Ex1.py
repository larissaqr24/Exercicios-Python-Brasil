'''Faça um Programa que leia um vetor de 5 números inteiros e mostre-os. '''

lista = []

for x in range(1,6):
    num = int(input(f'Digite o número {x}: '))
    lista.append(num)
print(lista)