'''
#14 - Faça um programa que peça 10 números inteiros, 
calcule e mostre a quantidade de números pares e a quantidade de números impares.
'''
cont=1
impar=0
par=0
while cont<11:
        nu=int(input(f'Informe o numero %d: '%cont))
        cont+=1
        div=nu%2
        if div!=0:
                impar+=1
        else:
                par+=1
print(f'Dos 10 numeros informados há {par} par e {impar} impar.')
