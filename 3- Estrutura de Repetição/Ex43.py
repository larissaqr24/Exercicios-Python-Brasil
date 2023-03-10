'''O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
Considere que o cliente deve informar quando o pedido deve ser encerrado.'''


print('Especificação / Código / Preço')
print('Cachorro Quente 100     R$ 1,20')
print('Bauru Simples   101     R$ 1,30')
print('Bauru com ovo   102     R$ 1,50')
print('Hambúrguer      103     R$ 1,20')
print('Cheeseburguer   104     R$ 1,30')
print('Refrigerante    105     R$ 1,00')

total_a_ser_pago = 0
pedido = 1
while pedido != 0:
    pedido = int(input('Informe o código do pedido: '))
    quantidade = int(input('Informe a quantidade: '))      
    if pedido == 100:
        total = 1.20 * quantidade
    elif pedido == 101:
        total= 1.30 * quantidade
    elif pedido == 102:
        total= 1.50 * quantidade
    elif pedido == 103:
        total= 1.20 * quantidade
    elif pedido == 104:
        total= 1.30 * quantidade
    elif pedido == 105:
        total =  1.00 * quantidade

    total_a_ser_pago += total      
print(f'Valor a ser pago: {total_a_ser_pago}')