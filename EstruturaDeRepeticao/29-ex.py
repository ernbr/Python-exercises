'''
#29 - O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. 
Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu uma tabela que contém o número de itens 
que o cliente comprou e ao lado o valor da conta. 
Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços.
Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá 
os preços de 1 até 50 produtos, conforme o exemplo abaixo:
Lojas Quase Dois - Tabela de preços
        1 - R$ 1.99
        2 - R$ 3.98
        ...
        50 - R$ 99.50   
'''
itens = 50
valor = 1.99
count = 0
print(f'Tabela de itens:')
while count<itens:
    count+=1
    print(f'{count} X {valor} = {count * valor:.2f}')
    
######################### - #########################

valor = 1.99
print(f'Tabela de itens:')
for i in range(50):
        i+=1
        print(f'{i} X {valor} = {i*valor:.2f}')
