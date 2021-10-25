'''
#42 - Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles 
estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. 
A entrada de dados deverá terminar quando for lido um número negativo.
'''
nu = 0
c1 = 0
c2 = 0
c3 = 0
c4 = 0

while nu >= 0:
    nu = int(input('Informe um numero: '))
    if nu > 100:
        print('informe números menor que 100 e maior que 0')
    if nu <= 25 and nu >=0:
        c1+=1
    elif nu <= 50 and nu >= 26:
        c2+=1
    elif nu <= 75 and nu >= 51:
        c2+=1
    elif nu <= 100 and nu >= 76:
        c2+=1

print(f'No conjunto[0-25] há {c1} numeros, [26-50] há {c2} numeros, [51-75] há {c3} numeros e [76-100] há {c4} numeros.')
