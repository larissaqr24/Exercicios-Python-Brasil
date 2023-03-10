'''Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, 
se seu argumento for positivo,e ‘N’, se seu argumento for zero ou negativo.'''

def poseneg(num):
    if num > 0:
        print('P')
    elif num <=0:
        print('N')

num = int(input('Digite um número: '))

poseneg(num)