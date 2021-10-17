'''#15 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, 
faça um programa que nos dê:
    Salário bruto.
    Quanto pagou ao INSS.
    Quanto pagou ao sindicato.
    O salário líquido.
Calcule os descontos e o salário líquido, conforme a tabela abaixo:
    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.'''

######################################## ########################################
 
salario_hora = int(input("Informe o valor do seu salário por hora: "))
horas_mes = int(input("informe quantas horas foram trabalhadas no mês: "))

salario_bruto = salario_hora * horas_mes

ir = salario_bruto * 0.11
inss = salario_bruto*0.08
sindicato = salario_bruto*0.05

def desconto_total():
    salario_liquido = salario_bruto - ir - inss - sindicato
    return salario_liquido

salario_total = desconto_total()

print(f"Nesse mês você trabalhou no total de {horas_mes} horas")
print(f"O seu salário bruto foi de R$ {salario_bruto}")
print(f"Você pagou ao Imposto de renda o total de R$ {ir}")
print(f"Você pagou ao INSS o total de R$ {inss}")
print(f"Você pagou ao Sindicato o total de R$ {sindicato}")
print(f"O seu salário liquido no mês foi de R$ {salario_total}")

######################################## ########################################
