'''
#13 - Faça um Programa que leia um número e exiba o dia correspondente da semana. 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
'''

dia = int(input("Informe um número correspondente a dia da semana: "))

if dia == 1:
    print(f'O número escolhido foi {dia}=Domingo')
elif dia == 2:
    print(f'O número escolhido foi {dia}=Segunda-feira')
elif dia == 3:
    print(f'O número escolhido foi {dia}=Terça-feira')
elif dia == 4:
    print(f'O número escolhido foi {dia}=Quarta-feira')
elif dia == 5:
    print(f'O número escolhido foi {dia}=Quinta-feira')
elif dia == 6:
    print(f'O número escolhido foi {dia}=Sexta-feira')
elif dia == 7:
    print(f'O número escolhido foi {dia}=Sabádo')
else:
    print(f'Valor inválido, informe um dia relativo aos dias da semana.')
