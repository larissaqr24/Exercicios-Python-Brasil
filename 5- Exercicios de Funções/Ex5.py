'''Faça um programa com uma função chamada somaImposto. 
A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas 
expressa em porcentagem e custo, que é o custo de um item antes do imposto. 
A função “altera” o valor de custo para incluir o imposto sobre vendas.'''


def somaImposto(imposto,valor):
    resultado = imposto + valor
    return resultado


valor = float(input('Informe o valor do item: '))
imposto = valor * 5 / 100
print(f'Imposto será de: {imposto}%')

print(somaImposto(imposto,valor))