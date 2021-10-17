'''
#7 - Faça um programa que leia 5 números e informe o maior número.
'''
numeros=1
maior=0
while numeros < 6:
        digite = int(input('Informe o numero %d:'%numeros))
        numeros+=1
        if digite > maior:
            maior=digite
print(f'O seu maior numero foi {maior}')
