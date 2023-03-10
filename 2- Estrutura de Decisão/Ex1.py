'''Faça um Programa que peça dois números e imprima o maior deles.'''

primeiro_num = int(input('Digite um número: '))
segundo_num =  int(input('Digite outro numero: '))
if primeiro_num > segundo_num:
    print(f'O número maior é: {primeiro_num}')
elif segundo_num > primeiro_num:
    print(f'O número maior é: {segundo_num}')
else:
    print('Os números são iguais.')