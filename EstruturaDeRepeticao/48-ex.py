'''
#48 - Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
  12376489
  => 98467321
'''
nu = int(input('Informe um numero inteiro: '))

for i in range(1,nu+1):
    print(f'{i}',end='')
print(' => ',end='')
while nu != 0:
    print(f'{nu}', end='')
    nu-=1
