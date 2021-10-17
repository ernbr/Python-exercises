'''
#34 - Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. 
Um número primo é aquele que é divisível apenas por um e por ele mesmo. 
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
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
    print(f'O {numero} não é um número primo.')

############################################################

count=1
while count < numero-1:
      count+=1
      if numero % count == 0 and numero!= count:
            print(f'multiplo de {count}')
            multiplo+=1

if (multiplo==0):
    print("O número é um número primo")
else:
    print(f'O {numero} não é um número primo.')
