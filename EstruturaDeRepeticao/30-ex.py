'''
#30 - O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, 
que já é um sucesso na sua loja de 1,99. 
Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, 
a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:

Preço do pão: R$ 0.18
Panificadora Pão de Ontem - Tabela de preços
1 - R$ 0.18
2 - R$ 0.36
...
50 - R$ 9.00
'''
itens = 50
valor = float(input(f'Informe o valor do pãozinho: '))
count = 0
print(f'Tabela de itens:')
while count<itens:
    count+=1
    print(f'{count} X {valor} = {count * valor:.2f}')
    
######################### - #########################

valor = float(input(f'Informe o valor do pãozinho: '))
print(f'Tabela de itens:')
for i in range(50):
        i+=1
        print(f'{i} X {valor} = {i*valor:.2f}')
