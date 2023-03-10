'''Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. 
Por exemplo: 127 -> 721.'''


def reverso(num):
    num = str(num)
    num = num[::-1]
    return int(num)

num = int(input('Digite um número: '))


print(reverso(num))