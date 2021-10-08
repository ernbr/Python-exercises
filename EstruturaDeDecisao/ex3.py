'''
#3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''
escolha = str(input("informe o seu sexo - F - Feminino, M - Masculino:")).strip().upper()
if escolha == "F":
    print ("Você escolheu F, de sexo Feminino.")
elif escolha == "M":
    print ("Você escolheu M, de sexo Masculino.")
else:
    print ("Sexo Inválido, por favor informe F para Feminino ou M para Masculino")
