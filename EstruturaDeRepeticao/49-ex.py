'''
#49 - Faça um programa que mostre os n termos da Série a seguir:
 S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
 Imprima no final a soma da série.
'''
n1 = 1
n2 = 1
print(f'S =', end="")

while True:
    print(f' {n1}/{n2} +', end="")
    soma = n1 + n2
    n1+=1
    n2+=2
    if n1 >= 20:
        break
print(f'= {soma}')
