'''
#28 - Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e 
o valor médio gasto em cada um deles. 
O usuário deverá informar a quantidade de CDs e o valor para em cada um.
'''
cds_quantidade = int(input('Informe a quantidade de CDs:'))
count=0
valor_cds = 0
while count < cds_quantidade:
    count+=1
    cds = int(input('Informe o valor do %d cd:'%count))
    valor_cds+=cds

media = valor_cds/cds_quantidade
print(f'Você gastou no total o valor de R$ {valor_cds} em cds.')
print(f'A média de R$ por cd é de R$ {media}')
