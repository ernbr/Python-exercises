'''
#9 - Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
'''
for i in range(1,51):
        div=i%2
        if div != 0:
                print(i)
##################################

#ALTERANATIVA
print(list(range(1,51,2)))
