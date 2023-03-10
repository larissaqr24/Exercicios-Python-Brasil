'''Faça um programa que leia 5 números e informe a soma e a média dos números.
'''

soma = 0
for x in range(1,6):
    num = int(input('Informe um número: '))
    soma += num
print(f'A soma dos valores é {soma}, e a média dos valores é {soma / 5}')

