'''
#25 - Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".
'''
print('Responda ao inquerito abaixo com Sim ou Nao!')
p1=input('Telefonou para a vítima?').upper()
p2=input('Esteve no local do crime?').upper()
p3=input('Mora perto da vítima?').upper()
p4=input('Devia para a vítima?').upper()
p5=input('Já trabalhou com a vítima?').upper()

resposta=p1,p2,p3,p4,p5

if resposta.count('SIM') + resposta.count('NAO')<=4:
    print('A sua resposta foi inválida, por gentileza responda todas apenas com Sim ou Nao')
else:
    if resposta.count('SIM') == 5:
        print('Você foi classificado como Assassino(a)')
    elif resposta.count('SIM') >=3:
        print('Você foi classificado como Cúmplice')
    elif resposta.count('SIM') >=2:
        print('Você foi classificado como Suspeito(a)')
    else:
        print('Você foi classificado como Inocente')

############################ ############################
