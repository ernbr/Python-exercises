'''
#41 - Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: 
valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
        Os juros e a quantidade de parcelas seguem a tabela abaixo:
        Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
        1       0
        3       10
        6       15
        9       20
        12      25
        
Exemplo de saída do programa:
        Valor da Dívida     Valor dos Juros     Quantidade de Parcelas      Valor da Parcela
        R$ 1.000,00         0                   1                           R$  1.000,00
        R$ 1.100,00         100                 3                           R$    366,00
        R$ 1.150,00         150                 6                           R$    191,67
        R$ 1.150,00         200                 9                           R$    ***
'''
divida = int(input('Informe o valor da divida: '))
parcelas = 12
juros = 0.05

print(f'Valor da Dívida\tValor dos Juros\tQuantidade de Parcelas\tValor da Parcela')
print(f'\t{divida:.2f}        \t0           \t 1              \t R$ {divida:.2f}')
qnt_parcelas = 0
while qnt_parcelas < parcelas:

    qnt_parcelas += 3
    juros += 0.05
    valor_juros = divida * juros
    valor_divida = divida + valor_juros
    Valor_Parcela = valor_divida/qnt_parcelas

    print(f'\t{valor_divida:.2f} \t     {valor_juros:.2f} \t         {qnt_parcelas} \t            R$ {Valor_Parcela:.2f}')
