'''
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
#19 -Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
'''
total=int(input('Informe uma quantidade de numero: '))

numeros=1
maior=1
menor=100
soma=0
while numeros <= total:
        digite = int(input('Informe o numero %d:'%numeros))
        numeros+=1
        if digite > maior:
            maior=digite

        if digite <menor:
            menor=digite

        soma=soma+digite

print(f'O seu maior numero foi {maior}')
print(f'O seu menor numero foi {menor}')
print(f'A soma dos numero foi {soma}')
