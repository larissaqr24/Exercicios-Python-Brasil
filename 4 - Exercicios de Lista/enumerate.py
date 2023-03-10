lista = ['Ravi', 'Lala', 'Lucas']

print('Quando preciso acessar apenas os valores das lista')
for x in lista:
    print(x)

print('#'*50)
print('Quando preciso acessar a posicao e o valor das listas')
for x, valor in enumerate(lista):
    print(x)
    print(valor)