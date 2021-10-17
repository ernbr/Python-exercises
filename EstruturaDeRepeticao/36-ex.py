'''
#36 - Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, 
mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, 
o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
 
    Montar a tabuada de: 5
    Começar por: 4
    Terminar em: 7
    
    Vou montar a tabuada de 5 começando em 4 e terminando em 7:
    5 X 4 = 20
    5 X 5 = 25
    5 X 6 = 30
    5 X 7 = 35
    Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.
'''
numero=int(input('Informe um numero para ser calculado: '))
tab_inicial=int(input('Informe por onde a tabuada deve começar: '))
tab_termina=int(input('Informe por até onde a tabuada deve terminar: '))

while tab_termina < tab_inicial:
        tab_inicial=int(input('Informe um numero menor que o final, onde a tabuada deve começar: '))
        tab_termina=int(input('Informe um numero maior que o numero de começo, onde a tabuada deve terminar: '))

print(f'Montar a tabuada de: {numero}')
print(f'Começar por: {tab_inicial}')
print(f'Terminar em: {tab_termina}')

for i in range(tab_inicial-1, tab_termina):
        i+=1
        print(f'{numero} X {i} = {numero*i}')
