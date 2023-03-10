'''Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.'''

num = []
par = []
impar = []
for x in range(5):
    num.append(int(input('Informe um numero: ')))

for n in num:
    if n % 2 == 0:
        par.append(n)   
    else:
        impar.append(n)

print(f'Números digitados: {num}')
print(f'Números pares: {par}')
print(f'Números impares: {impar}')