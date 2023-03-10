'''Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;'''

primeiro_lado = int(input('Digite o valor do primeiro lado: '))
segundo_lado = int(input('Digite o valor do segundo lado: '))
terceiro_lado = int(input('Digite o valor do terceiro lado: '))
if primeiro_lado == segundo_lado and terceiro_lado == primeiro_lado:
    print('Triângulo Equilátero.')
elif primeiro_lado != segundo_lado and terceiro_lado != primeiro_lado and terceiro_lado != segundo_lado:
    print('Triângulo Escaleno.')
else:
    print('Triângulo Isósceles.')