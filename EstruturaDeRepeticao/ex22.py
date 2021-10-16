'''
#21-Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
#22- Altere o programa de cálculo dos números primos,
informando, caso o número não seja primo, por quais número ele é divisível.
'''
numero=int(input('Informe um numero: '))
multiplo=0

for i in range(2,numero):
    if numero % i == 0:
        print(f'multiplo de {i}')
        multiplo+=1

if (multiplo==0):
    print("O número é um número primo")
else:
    print(f'Tem {multiplo} múltiplos acima de 2 e abaixo de {numero}')

##############################
count=1
while count < numero-1:
      count+=1
      if numero % count == 0 and numero!= count::
            print(f'multiplo de {count}')
            multiplo+=1

if (multiplo==0):
    print("O número é um número primo")
else:
    print(f'Tem {multiplo} múltiplos acima de 2 e abaixo de {numero}')
