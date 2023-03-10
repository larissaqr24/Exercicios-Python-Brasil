'''Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16'''

numero = input('Digite um numero inteiro positivo: ')

print(f'{numero[0:1]} centena(s), {numero[1:2]} dezena(s) e {numero[2:3]} unidade(s)')
# # Extraindo a unidade
# unidade = numero % 10

# # Eliminando a unidade de nosso número
# numero = (numero - unidade)/10

# # Extraindo a dezena
# dezena = numero % 10

# # Eliminando a dezena do número original, fica a centena
# numero = (numero - dezena)/10
# centena = numero

# # Fazendo ser inteiros
# dezena = int(dezena)
# centena = int(centena)
# print(centena,'centena(s),',dezena,'dezena(s) e',unidade,'unidade(s)')