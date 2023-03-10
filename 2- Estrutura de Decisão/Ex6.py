'''Faça um Programa que leia três números e mostre o maior deles.'''

primeiro_num = int(input('Digite um número: '))
segundo_num = int(input('Digite um número: '))
terceiro_num = int(input('Digite um número: '))
if primeiro_num > segundo_num:
    if primeiro_num > terceiro_num:
        print(f'O número maior é: {primeiro_num}')
    else:
        print(f'O número maior é o {terceiro_num}')
elif segundo_num > terceiro_num:
    print(f'O número maior é: {segundo_num}')
else:
    print(f'O número maior é o {terceiro_num}') 