'''
#19 - Faça um Programa que leia um número inteiro menor que 1000 
e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. 
Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''
numero = input('Informe um numero: ')
centena = 0
dezena = 0
unidade = 0

if len(numero) == 3:
    centena = int(numero[0])
    dezena = int(numero[1])
    unidade = int(numero[2])
elif len(numero)==2:
    dezena = int(numero[0])
    unidade = int(numero[1])
elif len(numero)==1:
    unidade = int(numero[0])
#mensagem 
if centena <= 1:
    lcentena = "centena"
else:
    lcentena = "centenas"
if dezena <=1:
    ldezena = "dezena"
else:
    ldezena = "dezenas"
if unidade <= 1:
    lunidade = "unidade"
else:
    lunidade = "unidades"

print (f'{numero} = {centena} {lcentena}, {dezena} {ldezena} e {unidade} {lunidade}.')
