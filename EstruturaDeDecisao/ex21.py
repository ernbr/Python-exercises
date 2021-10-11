'''
#21 - Faça um Programa para um caixa eletrônico.
O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.

Ex 1: Para sacar a quantia de 256 reais,
    o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Ex 2: Para sacar a quantia de 399 reais,
    o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1
'''

saque = int(input('Informe o valor a ser sacado, Min:R$ 10,00 e Max:R$ 600,00: '))

while (saque < 10 or saque >600):
    print('Valor digitado inválido, por gentileza, informe um valor mínimo de 10 reais e o máximo de 600 reais.')
    saque = int(input('Informe o valor a ser sacado, Min:R$ 10,00 e Max:R$ 600,00: '))

saque_100 = int(saque/100)
saque_50 = int((saque % 100)/50)
saque_10 = int((saque % 50)/10)
saque_5 = int((saque % 10)/5)
saque_1 = int((saque % 5)/1)

print(f'Será fornecido o total de {saque_100} notas de R$ 100,  {saque_50} de R$ 50, {saque_10} de R$ 10,'
              f' {saque_5} de R$ 5, e {saque_1} de R$ 1,00')
