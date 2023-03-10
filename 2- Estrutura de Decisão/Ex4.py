'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''

letra = input('Digite uma letra: ').lower()
vogais = ['a','e','i','o','u']

if len(letra) == 1:
    if letra in vogais: 
        print(f'A letra {letra} é uma vogal')
    else:
        print(f'A letra {letra} é uma consoante')
else:
    print('Favor informar apenas 1 letra!')


# if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u': 
#     print(f'A letra {letra} é uma vogal')
# else:
#     print(f'A letra {letra} é uma consoante')