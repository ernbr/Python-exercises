'''
#18 - Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
'''

data = str(input("Informe uma data válida em dd/mm/aaaa:"))

if len(data)==10:
    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6:10])

    valida = False
    #meses com 31 dias
    if (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
        if dia<31:
            valida = True
    #meses com 30 dias
    elif (mes==4 or mes==6 or mes==9 or mes==11):
        valida = True
    #meses bissextos
    elif mes==2:
        if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
            if dia <29:
                valida=True
        elif dia<28:
            valida = True

    if valida==True:
        print(f'A data informada foi {dia:02d}/{mes:02d}/{ano}.')
    else:
        print('A data informada é inválida.')
else:
    print('A data informada é inválida, informe a data no formato dd/mm/aaaa.')
