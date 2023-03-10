'''Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.'''

def numero(n):
    for x in range(1, n + 1):
        cont = 1
        while True:
            print(x, end=' ')
            if cont == x:
                break
            cont += 1
        print()
        
        
n = int(input('Digite um número: '))
numero(n)