'''
#39 - Faça um programa que leia dez conjuntos de dois valores, 
o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. 
Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, 
junto com suas alturas.
'''

count = 0
altura_max = 0
altura_min = 250

while count < 10:
    codigo = int(input('Informe o código do aluno: '))
    altura = int(input('Informe a sua altura em cm: '))

    if altura > altura_max:
        codigo_amax = codigo
        altura_max = altura

    if altura < altura_min:
        codigo_amin = codigo
        altura_min = altura

    count += 1

print(f'A altura do aluno mais alto é {altura_max}cm o código do aluno é: {codigo_amax}')
print(f'A altura do aluno mais baixo é {altura_min}cm o código do aluno é: {codigo_amin}')
