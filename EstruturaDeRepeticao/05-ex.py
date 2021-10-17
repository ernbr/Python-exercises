'''
#5 - Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
Valide a entrada e permita repetir a operação.
'''
pop_a = int(input('Informe a população A: '))
while pop_a <1:
    print('Informe uma população válida')
    pop_a = int(input('Informe a população A: '))

pop_b = int(input('Informe a população B: '))
while pop_b <1 or pop_b<pop_a:
    print('Informe uma população válida, a população B deverá ser maior que a A.')
    pop_b = int(input('Informe a população B: '))

taxa_a= float(input('Informe a taxa de crecimento da população A: '))
taxa_b= float(input('Informe a taxa de crecimento da população B: '))
ano=0

taxa_a = float(taxa_a/100)
taxa_b = float(taxa_b/100)

while pop_a <= pop_b:
    pop_a = int(pop_a + (pop_a * taxa_a))
    pop_b = int(pop_b + (pop_b * taxa_b))
    ano+=1

print (f'Levará cerca de {ano} anos para a populacao A:{pop_a} ultrapassar a B: {pop_b}.'
      f' A taxa de crescimento da pop A foi de {taxa_a:.1%} e a taxa de crescimento da B foi de {taxa_b:.1%}.')
