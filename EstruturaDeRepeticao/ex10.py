'''
#10 - Faça um programa que receba dois números inteiros e 
gere os números inteiros que estão no intervalo compreendido por eles.
'''
nu1=int(input('Informe um número: '))
nu2=int(input('Informe outro número: '))
while nu1>nu2:
        print('Informe o primeiro numero menor que o segundo')
        nu1=int(input('Informe um número: '))
        nu2=int(input('Informe outro número: '))
for i in range(nu1+1,nu2-1):
        i+=1
        print(i)
