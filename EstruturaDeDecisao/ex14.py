'''
#14- Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO”
se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
'''
nota1 = int(input("informe a primeira nota: "))
nota2 = int(input("Informe a segunda nota: "))
media = (nota1+nota2)/2

if media >=9 and media<10:
    print(f"Você recebeu as notas {nota1} e {nota2}, com média de {media} e A de conceito, sendo Aprovado.")
elif media >=7.5 and media<9:
    print(f"Você recebeu as notas {nota1} e {nota2}, com média de {media} e B de conceito, sendo Aprovado.")
elif media >=6 and media<7.5:
    print(f"Você recebeu as notas {nota1} e {nota2}, com média de {media} e C de conceito, sendo Aprovado.")
elif media >=4 and media<6:
    print(f"Você recebeu as notas {nota1} e {nota2}, com média de {media} e D de conceito, sendo Reprovado.")
elif media >= 0 and media < 4:
    print(f"Você recebeu as notas {nota1} e {nota2}, com média de {media} e E de conceito, sendo Reprovado.")
