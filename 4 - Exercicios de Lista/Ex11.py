'''Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
'''

vetor_a = []
vetor_b = []
vetor_c = []
vetor_d = []

for x in range(10):
    num = int(input('Digite um número: '))
    vetor_a.append(num)

for y in range(10):
    num2 = (input('Digite um caracter: '))
    vetor_b.append(num2) 

for z in range(10):
    num3 = (input('Digite um número: '))
    vetor_c.append(num3)

for x in range(10):
    vetor_d.append(vetor_a[x])
    vetor_d.append(vetor_b[x])
    vetor_d.append(vetor_c[x])

print(vetor_d)