'''
#13 - Faça um programa que peça dois números, base e expoente, 
calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
'''
nu1 = int(input('Informe a sua base: '))
nu2 = int(input('Informe o expoente: '))
print(f'{nu1} elevado a {nu2} = {nu1**nu2}')
pot=1

for i in range(nu2):
        i+=1
        pot*=nu1
print(f'{nu1} elevado a {nu2} = {pot}')
