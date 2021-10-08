'''
#10 - Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''

turno = str(input("digite o seu turno:M-matutino, V-Vespertino ou N- Noturno: ")).strip().upper()

if turno == "M":
    print ("BOm dia!")
elif turno == "V":
    print ("Boa tarde!")
elif turno == "N":
    print("Boa Noite!")
else:
    print("Valor inválido, por gentileza informe o turno correto")
