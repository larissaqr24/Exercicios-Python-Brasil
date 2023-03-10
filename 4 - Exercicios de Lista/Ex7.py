'''Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
'''
 
numeros = []
result = 1

for x in range(5):
    num = int(input('Digite um número: '))
    numeros.append(num)

for x in numeros:
    result *= x

soma = sum(numeros)
print(numeros)
print(f'A soma dos números da lista são: {soma}')
print(f'A multiplicação dos números da lista são: {result}')

