'''Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. 
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.'''

frase1 = input('Digite uma frase: ')
frase2 = input('Digite outra frase: ')
print(f'Tamanho da frase é: {len(frase1)}')
print(f'Tamanho da frase é: {len(frase2)}')

if len(frase1) == len(frase2) and frase1 == frase2:
    print('As duas frases possui o mesmo comprimento e o mesmo contéudo.')
elif frase1 != frase2:
    print('As duas frases possui comprimento diferentes e contéudo diferentes.')
