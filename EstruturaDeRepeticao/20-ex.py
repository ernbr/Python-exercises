'''
#20 - Altere o programa de cálculo do fatorial, 
permitindo ao usuário calcular o fatorial várias vezes e 
limitando o fatorial a números inteiros positivos e menores que 16.
'''
while 1==1:
    numero = int(input('Informe um numero para calculo do fatorial: '))
    while numero <= 0 or numero >16:
            numero = int(input('Numero incorreto Informe um numero para calculo do fatorial: '))
    contagem=1
    valor=1

    while contagem<=numero:
        valor*=contagem
        contagem+=1
    print(valor)
