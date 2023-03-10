'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.'''

primeiro_num = int(input('Digite um número inteiro: '))
segundo_num = int(input('Digite outro número inteiro : '))
terceiro_num = float(input('Digite um número decimal: '))
probl_a = (primeiro_num * 2) + (segundo_num / 2)
print(probl_a)
probl_b = (primeiro_num * 3) + terceiro_num 
print(probl_b)
probl_c = (terceiro_num * terceiro_num * terceiro_num)
print(probl_c)