'''
#6 - Faça um Programa que leia três números e mostre o maior deles.
'''
nu1 = int(input("informe um numero: "))
nu2 = int(input("informe outro numero: "))
nu3 = int(input("informe outro numero: "))

maior = 0
if nu1 >nu2 and nu1>nu3:
    maior = nu1
elif nu2 >nu1 and nu2>nu3:
    maior = nu2
else:
    maior = nu3

def numero_iguais():
    if nu1 == nu2:
        print(f"o numero 1 e 2 são iguais com o valor de {nu1} e {nu2}.")
    elif nu2 == nu3:
        print(f"o numero 2 e 3 são iguais com o valor de {nu2} e {nu3}.")
    elif nu1 == nu3:
        print(f"o numero 1 e 3 são iguais com o valor de {nu1} e {nu3}.")
    elif nu1 == nu2:
        print(f"Os numeros são iguais com o valor de {nu1},{nu2},{nu3}.")

numero_iguais()

print(f"o número {maior} foi o maior número digitado.")
