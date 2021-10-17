'''
#25 - Faça um programa que peça para n pessoas a sua idade, 
ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; 
e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada
'''
turma = (int(input('Informe a quantidade da turma: ')))
numeros = 1
soma = 0
media = 0

while numeros <= turma:
        idade=(int(input('Informe a sua idade: ')))
        numeros += 1
        soma += idade
        media = soma/turma

if media >= 0 and media  <= 25:
    print(f'A média de idade é de: {media:.1f} - A turma é Jovem')
elif media >= 26 and media  <= 60:
    print(f'A média de idade é de: {media:.1f} - A turma é Adulta')
else:
    print(f'A média de idade é de: {media:.1f} - A turma é Idosa')
