
'''
#40 - Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. 
Foram obtidos os seguintes dados:
    Código da cidade;
    Número de veículos de passeio (em 1999);
    Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
    *
    Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
    Qual a média de veículos nas cinco cidades juntas;
    Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
'''
indice_maior = 0
indice_menor = 0

media_veiculos = 0    #soma total de todos
media_acidentes = 0   #menos de 2000 veiculos
cidades_2k = 0

maior_indice = 0
menor_indice = 100

cidade = 5
count = 0

while count < cidade:
    cod_cidade = int(input('Informe o código da cidade: '))
    num_veiculos = int(input('Informe a quantidade de veiculos na cidade: '))
    num_acidentes = int(input('Informe a quantidade de acidentes com vitimas na cidade: '))
    media_veiculos += num_veiculos

    if num_acidentes > maior_indice:
        cod_maior_indice = cod_cidade
        maior_indice = num_acidentes

    if num_acidentes < menor_indice:
        cod_menor_indice = cod_cidade
        menor_indice = num_acidentes

    if num_veiculos < 2000:
        media_acidentes += num_acidentes
        cidades_2k += 1
    count+=1

print(f'O maior índice de acidentes de transito foi na cidade: {cod_maior_indice} com total de {maior_indice}')
print(f'O menor índice de acidentes de transito foi na cidade: {cod_menor_indice} com total de {menor_indice}')
print(f'A média de veículos nas cinco cidades juntas é de : {media_veiculos/cidade:.2f}')
print(f'A média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio é de {media_acidentes/cidades_2k:.2f} ')
