'''
#7 - Faça um Programa que leia três números e mostre o maior e o menor deles.
'''
nu1 = int(input("informe um numero: "))
nu2 = int(input("informe outro numero: "))
nu3 = int(input("informe outro numero: "))

def maior():
    maior=0
    if nu1>=nu2 and nu1>=nu3:
        maior=nu1
    elif nu2>=nu1 and nu2>=nu3:
        maior=nu2
    elif nu3>=nu1 and nu3>=nu2:
        maior=nu3
    return maior

def menor():
    menor=0
    if nu1<=nu2 and nu1<=nu3:
        menor=nu1
    elif nu2<=nu1 and nu2<=nu3:
        menor=nu2
    elif nu3<=nu1 and nu3<=nu2:
        menor=nu3
    return menor

def numero_iguais():
    if nu1 == nu2:
        print(f"o numero 1 e 2 são iguais com o valor de {nu1} e {nu2}.")
    elif nu2 == nu3:
        print(f"o numero 2 e 3 são iguais com o valor de {nu2} e {nu3}.")
    elif nu1 == nu3:
        print(f"o numero 1 e 3 são iguais com o valor de {nu1} e {nu3}.")
    elif nu1 == nu2:
        print(f"Os numeros são iguais com o valor de {nu1},{nu2},{nu3}.")

menor()
maior()
numero_iguais()

print(f"o número {maior()} é o maior número digitado e o menor foi o número {menor()}.")
