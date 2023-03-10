'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
'''
# Usando while
# num = int(input('Digite um número: '))
# fat = 1
# count = 2
# while count <= num:
#     fat = fat*count
#     count += 1

# print(f'O fatorial de {num} é = {fat}')

# Usando for
num = int(input('Digite um número: '))
result = 1
for x in range(1,num+1):
    result *= x
print(f'O fatorial de {num} é: {result}')

#Usando função
# def fatorial(num):
#     result = 1
#     for x in range(1,num+1):
#         result *= x

#     return result


# num = int(input('Digite um número: '))
# print(f'O fatorial de {num} é: {fatorial(num)}')
