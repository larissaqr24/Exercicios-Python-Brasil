'''Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.'''



nome = input('Digite seu nome: ')



for x in range(1,len(nome)+1):
    print(f"{nome[:x] : >{x}}")
 
# print('#'*50)
# y = 0
# for x in range(1,len(nome)+1):
#     print(f"{nome[y:x] : >{x}}")
#     y += 1