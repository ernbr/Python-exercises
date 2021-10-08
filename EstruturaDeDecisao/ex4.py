'''
#4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''
letra = str(input("informe uma letra a ser verificada:")).strip()
vogal = ["A","E","I","O","U"]

if letra in "AEIOU" or letra in "aeiou":
    print (f"A letra {letra} é uma vogal.")
elif (letra.isnumeric()):
    print (f"A letra {letra} é um número.")
else:
    print(f"A letra {letra} é uma consoante.")
