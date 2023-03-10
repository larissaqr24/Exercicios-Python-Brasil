'''Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
'''

def soma(a,b,c):
    resultado = a + b + c
    return resultado

num1 = int(input('Informe um número: '))
num2 = int(input('Informe um número: '))
num3 = int(input('Informe um número: '))
    

print(soma(num1,num2,num3))