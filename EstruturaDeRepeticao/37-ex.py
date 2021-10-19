'''
#37 - Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, o mais gordo e 
o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, 
sua altura e seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. 

Ao encerrar o programa também deve ser informados os códigos e valores do cliente mais alto, do mais baixo, 
do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes
'''
codigo = 0
altura = 0
peso = 0
count = 0

peso_min = 200
peso_max = 0
altura_max = 0
altura_min = float(3.0)

altura_total = 0
peso_total = 0

while True:
    codigo = int(input('Informe o seu código: '))
    if codigo == 0:
        media_altura = altura_total / (count - 1)
        media_peso = peso_total / (count - 1)
        print(f'A altura do cliente mais alto é {altura_max:.2f} o código do cliente é: {codigo_amax}')
        print(f'A altura do cliente mais baixo é {altura_min:.2f} o código do cliente é: {codigo_amin}')

        print(f'O peso do cliente mais pesado é {peso_max:.2f} kg o código do cliente é: {codigo_pmax}')
        print(f'O peso do cliente menos pesado é {peso_min:.2f} kg o código do cliente é: {codigo_pmin}')

        print(f' A média de altura dos clientes são : {media_altura:.2f} e de peso é : {media_peso:.2f} kg.  ')
        break
    count+=1

    altura_total += altura
    peso_total += peso
    altura = float(input('Informe a sua altura: '))
    peso = int(input('Informe o seu peso: '))

    if altura > altura_max:
        codigo_amax = codigo
        altura_max = altura

    if altura < altura_min:
        codigo_amin = codigo
        altura_min = altura

    if peso > peso_max:
        codigo_pmax = codigo
        peso_max = peso

    if peso < peso_min:
        codigo_pmin = codigo
        peso_min = peso
