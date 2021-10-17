'''
#26 - Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
    até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro

Gasolina:
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro 
    
Escreva um algoritmo que leia o número de litros vendidos, 
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
calcule e imprima o valor a ser pago pelo cliente 
sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''
comb = input('Informe o tipo de combustivel - A-álcool, G-gasolina: ').upper()
litros = int(input('Informe a quantidade de litros a ser abastecido: '))
preco=0

if comb == 'A':
    lcomb= 'álcool'
    preco = 1.90
    total = 0
    if litros <= 20:
        total = (preco-(preco*0.03)) * litros
    else:
        total = (preco-(preco*0.05)) * litros

elif comb == 'G':
    lcomb='gasolina'
    preco = 2.50
    total = 0
    if litros <= 20:
        total = (preco-(preco*0.04)) * litros
    else:
        total = (preco-(preco* 0.06)) * litros

print(f'Você abasteceu o total de {litros} litros de {lcomb} e irá pagar o total de R$ {total:.2f}.')

############################ ###########################
