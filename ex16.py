'''#16 - Faça um programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. '''

######################################## ########################################
import math

metros = int(input("Informe o tamanho em metros quadrados da área a ser pintada: "))
litros = metros/3
preco_lata = 80
capacidade_lata = 18
lata_necessarias = math.ceil(litros/capacidade_lata)

print (f'Você irá precisar {lata_necessarias:2d} latas de tinta no total de R$ {preco_lata*lata_necessarias}')

######################################## ########################################
