'''#17 - Faça um Programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 
ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
Comprar apenas latas de 18 litros;
Comprar apenas galões de 3,6 litros;
Misturar latas e galões, de forma que o desperdício de tinta seja menor. 
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. '''

######################################## ########################################
import math

metros = int(input("Informe o tamanho em metros quadrados da área a ser pintada: "))
litros = metros/6
preco_lata = 80
preco_galao = 25.00
capacidade_galao = 3.6
capacidade_lata = 18
lata_necessarias = math.ceil(litros/capacidade_lata)
galao_necessarios = math.ceil(litros/capacidade_galao)

print (f'Você irá precisar de {lata_necessarias} lata de tinta no total de R$ {preco_lata*lata_necessarias}')
print (f'Ou pode usar {galao_necessarios} galão de tinta no total de R$ {preco_galao*galao_necessarios}')

#mistura latas e tintas

mix_latas = int(litros/18)
sobra_mix = ((litros % 18)*1.1)    #Com acrecimo de 10%
mix_galao = math.ceil(sobra_mix/3.6)

preco_mix_latas = mix_latas*80
preco_mix_galao = mix_galao*25

print (f'Você também pode usar {mix_latas} latas e {mix_galao} galão no total de '
       f'R$ {preco_mix_latas+preco_mix_galao}')

######################################## ########################################
