'''
#32 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
'''
numero = int(input('Informe um numero a ser fatorado: '))
count = numero
total = 1
print(f'Calculando fatorial de {numero}! = ', end='')
while count >0:
    total *= count
    print(f'{count}', end='')
    print(f' x ' if count > 1 else ' = ', end='')
    count -= 1
print(f'{total}')
