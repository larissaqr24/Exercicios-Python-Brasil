'''Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. 
Imprima as consoantes. ''' 


consoantes = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','w','y','z']
count = 0
for x in range(10):
    carac = input('Digite um caracter: ')
    if carac in consoantes:
        count += 1
print(f'Exite {count} consoantes.')


    