'''
#11 - Faça um programa que receba dois números inteiros e 
gere os números inteiros que estão no intervalo compreendido por eles.
#11 - Altere o programa anterior para mostrar no final a soma dos números.
'''
nu1=int(input('Informe um número: '))
nu2=int(input('Informe outro número: '))
soma=0
while nu1>nu2:
        print('Informe o primeiro numero menor que o segundo')
        nu1=int(input('Informe um número: '))
        nu2=int(input('Informe outro número: '))
for i in range(nu1,nu2-1):
        i+=1
        print(i)
        soma+=i
print(f'A soma dos numeros entre {nu1} e {nu2} é = {soma}')

