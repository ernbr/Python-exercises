'''
#33 - O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa 
que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, 
bem como a média das temperaturas.
'''

total=int(input('Informe uma quantidade de temperaturas a serem calculadas: '))

numeros=1
maior=1
menor=100
soma=0

while numeros <= total:
        digite = int(input('Informe uma temperatura: '))
        numeros+=1
      
        if digite > maior:
            maior=digite
        if digite <menor:
            menor=digite
            
        soma+=digite
media=soma/total

print(f'A sua maior temperatura foi {maior}')
print(f'A sua menor temperatura foi {menor}')
print(f'A media de temperatura foi de {media}')
