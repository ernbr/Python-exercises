'''
#27 - Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
receberá ainda um desconto de 10% sobre este total. 
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas 
e escreva o valor a ser pago pelo cliente.
'''
fruta = input('Informe a fruta: ')
kg = int(input('Informe o peso da fruta em kg: '))

preco5 = 2.50
preco5m = 2.20

if fruta == 'morango':
    preco5 = 2.50
    preco5m = 2.20

elif fruta == 'maca':
    preco5 = 1.80
    preco5m = 1.50

if kg <=5:
    total = preco5*kg
else:
    total = preco5m*kg

if total >= 25 or kg >=8:
    total = total -(total*0.10)

print(f'Você comprou: {kg}kg de {fruta} no total de R$ {total}.')
