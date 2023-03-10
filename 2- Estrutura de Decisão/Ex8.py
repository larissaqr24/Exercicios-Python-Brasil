'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.'''

primeiro_produto = float(input('Digite o valor do produto: '))
segundo_produto = float(input('Digite o valor do produto: '))
terceiro_produto = float(input('Digite o valro do produto: '))
if primeiro_produto < segundo_produto:
    if primeiro_produto < terceiro_produto:
        print(f'Você deve comprar o : {primeiro_produto}')
    else:
        print(f'Você deve comrpar o: {terceiro_produto}')
elif segundo_produto < terceiro_produto:
    print(f'Você deve comprar o: {segundo_produto}')
else:
    print(f'Você deve comprar o:  {terceiro_produto}')