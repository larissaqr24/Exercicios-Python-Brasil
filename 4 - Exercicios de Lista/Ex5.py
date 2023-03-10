'''Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.'''

num = []
par = []
impar = []
for x in range(20):
    n= int(input('Digite um número: '))
    num.append(n)
    if n % 2 == 0:
        par.append(n)   
    else:
        impar.append(n)
print(f'Números digitados: {num}')
print(f'Números pares: {par}')
print(f'Números impares: {impar}')