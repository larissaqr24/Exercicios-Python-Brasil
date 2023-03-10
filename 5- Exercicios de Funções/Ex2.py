'''Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.'''

def numero(n):
    for x in range(1, n + 1):
        count = 1
        while True:
            print(count, end=' ')
            if count == x:
                break
            count += 1
        print()
        
        
n = int(input('Digite um número: '))
numero(n)