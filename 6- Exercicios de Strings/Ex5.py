'''Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.'''


nome = input('Digite seu nome: ')
for x in range(1,len(nome)):
    print(f"{nome[0:-x] : <{x}}")
