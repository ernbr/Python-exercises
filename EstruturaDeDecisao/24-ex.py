'''
#24 - Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
'''
numero1 = float(input('Informe um número: '))
numero2 = float(input('Informe outro número: '))
escolha = int(input('Digite o numero da operação a ser realizada:'
                '1-(/) divisão, 2-(+)soma, 3-(*)Multiplicação ou 4-(-) Subtração '))

while (escolha<1 or escolha>4):
    print(f'Numero inválido!')
    escolha = input('Digite o numero da operação a ser realizada:'
                    '1-(/) divisão, 2-(+)soma, 3-(*)Multiplicação ou 4-(-) Subtração ')

if escolha == 1:
    resultado = float(numero1/numero2)

elif escolha == 2:
    resultado = float(numero1 + numero2)

elif escolha == 3:
    resultado = float(numero1 * numero2)

elif escolha == 4:
    resultado = float(numero1 - numero2)


if resultado == round(resultado):
    print(f'O resultado: {resultado:.2f} é um número inteiro')
else:
    print(f'O resultado: {resultado:.2f} é um número decimal')

div = resultado % 2
if div != 0:
    print(f'O resultado: {resultado:.2f} é um número impar')
else:
    print(f'O resultado: {resultado:.2f} é um número par')

if resultado <0:
    print(f'O resultado: {resultado:.2f} é um número negativo')
else:
    print(f'O resultado: {resultado:.2f} é um número positivo')
