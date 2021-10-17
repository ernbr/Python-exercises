'''
23- Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
'''
numero2=int(input('Informe um numero: '))
numero=1
div=0
while numero < numero2:
    numero+=1
    multiplo=0
    count=1

    while count < numero:
          count+=1
          if numero % count == 0 and numero!= count:
                multiplo+=1
                div += 1
    if (multiplo==0):
        print(f'Até o {numero2} - O numero {numero} é numero Primo')
        div += 1
print(f'Foram feitas {div} divisoes')
