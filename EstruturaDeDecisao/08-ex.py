'''
#8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
sabendo que a decisão é sempre pelo mais barato.
'''
produto1 = int(input("informe o preço do primeiro produto: "))
produto2 = int(input("informe o preço do segundo produto: "))
produto3 = int(input("informe o preço do terceiro produto: "))

def menor():
    if produto1 <produto2 and produto1<produto3:
        print(f"o produto 1 é o menor preço com o valor de {produto1}.")
    elif produto2 <produto1 and produto2<produto3:
        print(f"o produto 2 é o menor preço com o valor de {produto2}.")
    elif produto3 <produto1 and produto3<produto2:
        print(f"o produto 3 é o menor preço com o valor de {produto3}.")

        #numero iguais
    elif produto1 == produto2 and produto1<produto3:
        print(f"o produto 1 e 2 são iguais com o menor preço de {produto1} e {produto2}.")
    elif produto2 == produto3 and produto2 < produto1:
        print(f"o produto 2 e 3 são iguais com o menor preço de {produto2} e {produto3}.")
    elif produto1 == produto3 and produto1 < produto2:
        print(f"o produto 1 e 3 são iguais com o menor preço de {produto1} e {produto3}.")
    elif produto1 == produto2 and produto1 == produto3:
        print(f"Os produtos são iguais com o valor de {produto1},{produto2},{produto3}.")
menor()
