'''
#35 - Encontrar números primos é uma tarefa difícil. 
Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.
'''

numero2=int(input('Informe um numero: '))
numero=1
print(f'Até o {numero2} - Os numeros primos são: ', end="")

while numero < numero2:
    numero+=1
    multiplo=0
    count=1

    while count < numero:
          count+=1
          if numero % count == 0 and numero!= count:
                multiplo+=1

    if (multiplo==0):
        print(f'{numero}, ', end="")

