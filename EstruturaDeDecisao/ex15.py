'''
#15 - Faça um Programa que peça os 3 lados de um triângulo. 
O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
    Dicas:
    
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    
    Triângulo Isósceles: quaisquer dois lados iguais;
    !Triângulo Equilátero: três lados iguais;
    !Triângulo Escaleno: três lados diferentes;
'''
lado1 = int(input("Informe o lado de um Triângulo: "))
lado2 = int(input("Informe outro lado do Triângulo: "))
lado3 = int(input("Informe outro lado do Triângulo: "))

if (lado1+lado2<lado3)or(lado1+lado3<lado2) or(lado2+lado3<lado1):
    print("Isso não é um Triângulo")

elif (lado1==lado2) and (lado1==lado3):
    print("Isso é um Triângulo equilatero")

elif (lado1==lado2) or (lado2==lado3):
    print("Isso é um Triângulo Isósceles")

elif (lado1!=lado2!=lado3):
    print("Isso é um Triângulo escaleno")
