'''Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.'''

sexo = input('Digite seu sexo: ').upper()
# sexo = sexo.upper()
if sexo == 'F': 
    print('Sexo Feminino')
elif sexo == 'M':
    print('Sexo Masculino')
else:
    print('Sexo inválido.')