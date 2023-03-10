'''Faça um Programa que leia um vetor A com 10 números inteiros, 
calcule e mostre a soma dos quadrados dos elementos do vetor.
'''

soma_dos_quadrados = 0
for x in range(10):
    soma_dos_quadrados += int(input(f'Digite o {x+1}º numero inteiro: ')) ** 2
print(f'A soma dos quadrados dos numeros digitados é {soma_dos_quadrados}')