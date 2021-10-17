'''
#11 -As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e
lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um progr que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,baseado no salário atual:
    o   salários até R$ 280,00 (incluindo) : aumento de 20%
    o   salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    o   salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    # - salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
        o   salário antes do reajuste;
        o   percentual de aumento aplicado;
        o   valor do aumento;
        o   novo salário, após o aumento.
'''
salario_atual = int(input("Informe o seu salario: "))
novo_salario = 0
print(f"O seu salario antes do ajuste era de R$ {salario_atual:.2f}.")

if salario_atual <= 280:
    novo_salario = salario_atual+(salario_atual*0.2)
    print(f'Devido ao valor do seu salário atual, você irá receber o total de 20% de aumento.')

elif salario_atual > 280 and salario_atual <= 700:
    novo_salario = salario_atual+(salario_atual*0.15)
    print(f'Devido ao valor do seu salário atual, você irá receber o total de 15% de aumento.')

elif salario_atual > 700 and salario_atual <= 1500:
    novo_salario = salario_atual+(salario_atual*0.10)
    print(f'Devido ao valor do seu salário atual, você irá receber o total de 10% de aumento.')

elif salario_atual > 1500:
    novo_salario = salario_atual+(salario_atual*0.5)
    print(f'Devido ao valor do seu salário atual, você irá receber o total de 5% de aumento.')

print(f"Com esse reajuste, você irá receber o total de R$ {novo_salario - salario_atual:.2f} de aumento"
      f" e seu salárío passará a ser de R$ {novo_salario:.2f} ")
