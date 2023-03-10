'''Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.'''

vetor_a = []
vetor_b = []
vetor_c = []
for x in range(10):
    num = int(input('Digite um número: '))
    vetor_a.append(num)

for y in range(10):
    num2 = (input('Digite um caracter: '))
    vetor_b.append(num2) 

for x in range(10):
    vetor_c.append(vetor_a[x])
    vetor_c.append(vetor_b[x])

print(vetor_c)