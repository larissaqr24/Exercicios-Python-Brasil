'''Faça um Programa que leia três números e mostre o maior e o menor deles.'''

primeiro_num = int(input('Digite um número: '))
segundo_num = int(input('Digite um número: '))
terceiro_num = int(input('Digite um número: '))

# lista = [primeiro_num, segundo_num, terceiro_num]
# lista.sort()
# print(f'O menor numero é: {lista[0]}')
# print(f'O maior numero é: {lista[2]}')

menor = 0
maior = 0

if primeiro_num == segundo_num and primeiro_num == terceiro_num:
    print('Todos os números são guais.')
else:
    if primeiro_num > segundo_num:
        if primeiro_num > terceiro_num:
            maior = primeiro_num
            if segundo_num < terceiro_num:
                menor = segundo_num
            else:
                menor = terceiro_num
        else:
            maior = terceiro_num
    elif segundo_num > terceiro_num:
        maior = segundo_num
        if terceiro_num < primeiro_num:
            menor = terceiro_num
    else:
        maior = terceiro_num
        menor = primeiro_num

    print(f'O número maior é o {maior}')
    print(f'O número menor é o {menor}')

