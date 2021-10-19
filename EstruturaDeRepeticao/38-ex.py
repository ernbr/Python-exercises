'''
#38 - Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
    A - Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
    B - Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
    C - A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
        Faça um programa que determine o salário atual desse funcionário.
        Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
'''
salario = int(input('Salario inicial: '))
ano = 1995
taxa = 1.5/100

while ano < 2021:
    salario_total = salario + (salario * taxa)
    taxa = taxa * 2
    ano += 1

    print (f'salario_total :{salario_total:.2f}', end='')
    print(f' ano: {ano}')
