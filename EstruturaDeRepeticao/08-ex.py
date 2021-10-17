'''
#8 - Faça um programa que leia 5 números e informe a soma e a média dos números.
'''
numeros=1
soma=0

while numeros < 6:
        digite = int(input('Informe o numero %d:'%numeros))
        numeros +=1
        soma += digite

media= soma/(numeros-1)
print(f'A soma dos numeros é: {soma}')
print(f'A média dos numeros é: {media:.2f}')
