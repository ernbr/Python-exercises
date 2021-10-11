'''
#22 - Faça um Programa que peça um número inteiro e determine se ele é par ou impar. 
Dica: utilize o operador módulo (resto da divisão).
'''

numero = int(input('Informe um número: '))
div = numero%2
if div!= 0:
    print(f'O número {numero} é um número impar')
else:
    print(f'O número {numero} é um número par')
