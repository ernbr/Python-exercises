############################    ############################
'''
#9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''
nu1 = int(input("informe um numero: "))
nu2 = int(input("informe outro numero: "))
nu3 = int(input("informe outro numero: "))
lista = [nu1,nu2,nu3]
lista.sort()

print(f'A ordem dos números digitados são {lista}.')

############################    ########################################################    ############################
'''
#9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''
nu1 = int(input("informe um numero: "))
nu2 = int(input("informe outro numero: "))
nu3 = int(input("informe outro numero: "))

def ordem():
    if nu1 < nu2 and nu1 < nu3 and nu2 < nu3:
        ordem = (nu1 , nu2, nu3)
    elif nu2 < nu1 and nu2 < nu3 and nu1 < nu3:
        ordem = (nu2, nu1, nu3)
    elif nu3 < nu1 and nu3 < nu2 and nu2 < nu1:
        ordem = (nu3, nu2, nu1)
    elif nu1 < nu2 and nu1 < nu3 and nu3 < nu2:
        ordem = (nu1, nu3, nu2)
    elif nu2 < nu1 and nu2 < nu3 and nu3 < nu1:
        ordem = (nu2, nu3, nu1)
    elif nu3 < nu1 and nu3 < nu2 and nu1 < nu2:
        ordem = (nu3, nu1, nu2)

    return ordem
print(f"A ordem dos numeros são {ordem()}.")
