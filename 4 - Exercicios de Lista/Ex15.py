'''Faça um programa que leia um número indeterminado de valores, correspondentes a notas, 
encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). 
Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;'''

numeros = []

while True:
    num = int(input('Informe um número: '))
    numeros.append(num)
    if num == -1:
        numeros.remove(-1)
        break

quantidade = len(numeros)
print(f'Foram digitados {quantidade} valores')

print(numeros)

novo_numeros = numeros[:: -1]
print(novo_numeros) #um abaixo do outro

soma = sum(numeros)
print(f'A soma dos valores é: {soma}')

media = soma / len(numeros)
print(f'A média dos valores é: {media}')

for x, valor in enumerate(numeros):
    if valor >= media:
        print(f'Valores acima da média: {valor} ')

for x, valor in enumerate(numeros):
    if valor <= 7:
        print(f'Valores abaixo de 7 são: {valor}')

print('Programa encerrado')