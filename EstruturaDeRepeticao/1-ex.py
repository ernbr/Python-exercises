'''
#1 - Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''
nota = int(input('Informe uma nota de zero a dez:'))

while nota<0 or nota >10:
    print(f'A nota digitada é invalida, por favor digite uma nota de 0 a 10.')
    nota = int(input('Informe uma nota de zero a dez:'))
print(f'A nota digitada foi {nota}')
