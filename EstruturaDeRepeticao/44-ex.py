'''
#44 - Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. 
Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

    Faça um programa que calcule e mostre:
    O total de votos para cada candidato;
    O total de votos nulos;
    O total de votos em branco;
    A percentagem de votos nulos sobre o total de votos;
    A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
'''
votos = 0
soma_1 = 0
soma_2 = 0
soma_3 = 0
soma_4 = 0
soma_nulo = 0
soma_branco = 0

while True:
        candidato =(int(input('Informe O numero do seu candidato:\n 1- Jose/ 2- João/ 3- Maria/ 4-Enzo\n'
                              '// 5- Voto Nulo e 6- Voto em Branco. '
                              '// 0 - encerra o programa: ')))
        votos += 1

        if candidato == 1:
            soma_1 += 1
        elif candidato == 2:
            soma_2 += 1
        elif candidato == 3:
            soma_3 += 1
        elif candidato == 4:
            soma_4 += 1
        elif candidato == 5:
            soma_nulo += 1
        elif candidato == 6:
            soma_branco += 1
        else:
            break

print(f'Recebemos o total de = {votos} votos \n'
      f'O candidato 1 recebeu o total de {soma_1} votos, \n'
      f'o candidato 2 recebeu o total de {soma_2} votos, \n'
      f'o candidato 3 recebeu o total de {soma_3} votos, \n'
      f'e o candidato 4 recebeu o total de {soma_4} votos.\n'
      f'Tiveram o total de votos {soma_nulo} nulos e o total de votos {soma_branco} em branco.\n')

media_nulo = (soma_nulo/votos)*100
media_branco = (soma_branco/votos)*100
print(f'A percentagem de votos nulos sobre o total de votos foi de: {media_nulo:.2f}')
print(f'A percentagem de votos em branco sobre o total de votos foi de: {media_branco:.2f}')
