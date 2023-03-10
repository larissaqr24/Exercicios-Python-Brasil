'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).'''

tamanho_arquivo = int(input('Tamanho de um arquivo para download em MB: '))
velocidade = int(input('Qual é a velocidade do link: ')) #em horas
tempo = (tamanho_arquivo / (velocidade/8)) #minutos
print(f'{tempo}')
minutos = tempo / 60
print(f'O download será feito em: {minutos} minutos')
