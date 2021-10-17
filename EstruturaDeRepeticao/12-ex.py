'''
#12 -Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
        5 X 1 = 5
        5 X 2 = 10
        ...
        5 X 10 = 50
'''
nu = int(input('Informe um número entre 1 a 10: '))
while nu <= 0 or nu > 10:
        nu = int(input('Número inválido: - Informe um número entre 1 a 10: '))

print(f'Tabuada de {nu}:')
for i in range(10):
        i+=1
        print(f'{nu} X {i} = {nu*i}')
