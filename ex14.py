'''#14 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas. '''

######################################## ########################################

peso_peixe = int(input("informe o peso do peixe: "))
excesso_peso = 0
if (peso_peixe > 50):
    excesso_peso= peso_peixe-50
else:
    excesso_peso = 0

multa_peso = 0
if (excesso_peso>=1):
        multa_peso+= 4
        print(f'O seu peixe estourou o limite estabelecido, '
              f'Você deverá pagar uma multa no total de {excesso_peso*multa_peso}')
else:
    print(f'O seu peixe não estourou o limite estabelecido e não pagará multa.')

######################################## ########################################
