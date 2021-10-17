'''
#28 - O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                              Até 5 Kg           Acima de 5 Kg
        File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
        Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
        Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
porém não há limites para a quantidade de carne por cliente. 

Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
 
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, 
valor do desconto e valor a pagar.
'''

carne = input('Informe a carne que deseja, File Duplo ,Alcatra ou Picanha : ')
kg = int(input('Informe o peso em kg: '))
tipo_pagamento = input('Informe o tipo de pgto, caso seja cartao Tabajara, informe apenas tabajara: ')

preco5 = 4.90
preco5m = 5.80

if carne == 'File Duplo':
    preco5 = 4.90
    preco5m = 5.80

elif carne == 'Alcatra':
    preco5 = 5.90
    preco5m = 6.850

elif carne == 'Picanha':
    preco5 = 6.90
    preco5m = 7.80

if kg <=5:
    total = preco5*kg
else:
    total = preco5m*kg

if tipo_pagamento == 'tabajara':
    total = total -(total*0.05)
    print(f'Você comprou: {kg} kg de {carne} no total de R$ {total}, com o desconto de 5% do seu cartão Tabajara.')
else:
    print(f'Você comprou: {kg} kg de {carne} no total de R$ {total}.')

