'''
#43 - O cardápio de uma lanchonete é o seguinte:
    Especificação   Código  Preço
    Cachorro Quente 100     R$ 1,20
    Bauru Simples   101     R$ 1,30
    Bauru com ovo   102     R$ 1,50
    Hambúrguer      103     R$ 1,20
    Cheeseburguer   104     R$ 1,30
    Refrigerante    105     R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
Considere que o cliente deve informar quando o pedido deve ser encerrado.
'''
cod100 = 1.20
cod101 = 1.30
cod102 = 1.50
cod103 = 1.20
cod104 = 1.30
cod105 = 1.00
valor = 0

while True:
    pedido = int(input('Informe o código do lanche que você deseja e 0 para concluir o pedido: '))
    quantidade = int(input('Informe a quantidade de lanches de acordo com o código: '))

    if pedido == 100:
        quantidade100 = quantidade
        valor += 1.20 * quantidade
        print(f'O valor desse pedido é de R$ {quantidade100*cod100:.2f}')
    if pedido == 101:
        quantidade101 = quantidade
        valor += 1.30 * quantidade
        print(f'O valor desse pedido é de R$ {quantidade101*cod100:.2f}')
    if pedido == 102:
        quantidade102 = quantidade
        valor += 1.50 * quantidade
        print(f'O valor desse pedido é de R$ {quantidade102*cod100:.2f}')
    if pedido == 103:
        quantidade103 = quantidade
        valor += 1.20 * quantidade
        print(f'O valor desse pedido é de R$ {quantidade103*cod100:.2f}')
    if pedido == 104:
        quantidade104 = quantidade
        valor += 1.30 * quantidade
        print(f'O valor desse pedido é de R$ {quantidade104*cod100:.2f}')
    if pedido == 105:
        quantidade105 = quantidade
        valor += 1.00 * quantidade
        print(f'O valor desse pedido é de R$ {quantidade105*cod100}')
    if pedido == 0:
        break

print (f'O valor total do seu pedido foi de R$: {valor}')
