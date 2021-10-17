'''
#17 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
Ex.: 5!=5.4.3.2.1=120
'''
numero = int(input('Informe um numero para calculo do fatorial: '))
contagem=1
valor=1
while contagem<=numero:
    valor*=contagem
    contagem+=1
print(valor)


############################################################
numero = int(input('Informe um numero para calculo do fatorial: '))
contagem=1
for i in range(1,numero+1):
    contagem *= i

print(contagem)
