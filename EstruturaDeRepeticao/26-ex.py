'''
#26 - Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
'''
eleitores = (int(input('Informe a quantidade de eleitores: ')))
numeros = 0
soma_1 = 0
soma_2 = 0
soma_3 = 0

while numeros < eleitores:
        candidato =(int(input('Informe O numero do seu candidato: ')))
        numeros += 1

        if candidato == 1:
            soma_1 += 1
        elif candidato == 2:
            soma_2 += 1
        else:
            soma_3 += 1

print(f'O candidato 1 recebeu o total de {soma_1} votos, \n'
      f'O candidato 2 recebeu o total de {soma_2} votos, \n'
      f'e o candidato 3 recebeu o total de {soma_3} votos')
'''
