'''
#24 -Faça um programa que calcule o mostre a média aritmética de N notas.
'''
notas=(int(input('Informe a quantidade de notas:')))
numeros=1
soma=0

while numeros < notas+1:
        digite = int(input('Informe a nota %d:'%numeros))
        numeros +=1
        soma += digite

media= soma/(numeros-1)
print(f'A média dos numeros é: {media:.2f}')
