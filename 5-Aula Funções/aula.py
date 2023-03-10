import matematica
# # Criando uma funçao
# def soma(a, b):
#     resultado = a + b
#     return resultado


# print(matematica.soma(4, 6))

nota_aluno = (10, 6, 8, 9, 10)


def escola(aluno, cidade='Udi', *notas):
    print(f'Aluno: {aluno}')
    print(f'Cidade: {cidade}')
    for x in notas:
        print(f'Notas: {x}')


escola('Larissa', 'Udi', nota_aluno)


# Argumentos das funçoes:
# pode ter argumentos simples
# E argumentos complexos

# *args = vem em formato de tuplas
# **kwargs = vem em formato de dicionarios


# ## Estrutura
# Primeiro os argumentos simples, depois os args e depois os kwargs
