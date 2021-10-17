'''#13 - Tendo como dado de entrada a altura (h) de uma pessoa, 
construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''

######################################## ########################################

altura = float(input ("Informe a sua altura: "))
sexo = str(input("Informe o seu sexo, (H) para Homem e (M) para Mulher:").upper())

if (sexo == "H"):
        print (f'O seu peso ideal de acordo com a sua altura é {(72.7*altura)-58 :.2f}')
elif(sexo == "M"):
        print (f'O seu peso ideal de acordo com a sua altura é {(62.7*altura)-58 :.2f}')
######################################## ########################################
