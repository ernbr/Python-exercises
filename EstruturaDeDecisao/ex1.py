'''
#1 - Faça um Programa que peça dois números e imprima o maior deles.
'''
nu1 = int(input("informe um numero: "))
nu2 = int(input("Informe outro numero: "))

if nu1>nu2:
    print(f"O numero {nu1} é maior que o numero {nu2}")
elif nu2>nu1:
    print(f"O numero {nu2} é maior que o numero {nu1}")
else:
    print (f"O número {nu1} é igual ao {nu2}.")
