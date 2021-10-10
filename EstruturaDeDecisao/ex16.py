'''
#16 - Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, 
sendo encerrado;

Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''
import math

a = int(input("Informe o valor de A: "))

if a==0:
    print("Isso não é uma equação de segundo grau!")
else:
    b = float(input("Informe o segundo valor: "))
    c = float(input("Informe o terceiro valor: "))

delta = b*b-(4*a*c)
raiz1 = 0
raiz2 = 0

if delta <0:
    print("A equação não possui raizes reais.")
elif delta == 0:
    raiz1 = -b / (2 * a)
    print(f"A equação possui apenas uma raiz real: {raiz1}.")
elif delta >0:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"A equação possui 2 raizes reais: {raiz1:.0f} e {raiz2:.0f}.")
