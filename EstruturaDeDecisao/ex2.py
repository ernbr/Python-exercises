'''
#2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
'''
nu1 = int(input("informe um numero: "))
if nu1>0:
    print (f"O numero {nu1} é positivo.")
elif nu1<0:
    print (f"O numero {nu1} é negativo.")
else:
    print (f"O número {nu1} é igual a 0.")
