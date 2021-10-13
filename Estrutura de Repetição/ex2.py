'''
#2 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações.
'''
usuario = input('Informe o seu usuario:')
senha = input('Informe a sua senha:')

while senha== usuario:
    print(f'A sua senha não deve ser igual ao seu usuario, por gentileza, informe uma nova senha.')
    senha = input('Informe a sua senha:')

print(f'Usuario e senha permitido')
