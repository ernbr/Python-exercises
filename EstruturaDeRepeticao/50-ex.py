'''
#50 - Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, 
Faça um programa que calcule o valor de H com N termos.
'''
h1 = 1
n2 = 1
termos = int(input('Informe o numeros de termos: '))

print(f'H = 1 +', end="")
count = 0

while count != termos:
    print(f' {h1}/{n2} +', end="")
    n2+=1
    count+=1

print(f'= {h1+n2-1}')
