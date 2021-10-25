'''
#45 -Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, 
o programa deve perguntar ao aluno a resposta de cada questão e 
ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota 
(atribuir 1 ponto por resposta certa). 

Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. 
Após todos os alunos terem respondido informar:

Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.

Gabarito da Prova:

    01 - A
    02 - B
    03 - C
    04 - D
    05 - E
    06 - E
    07 - D
    08 - C
    09 - B
    10 - A
Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova 
antes dos alunos usarem o programa.
'''
for a in range (1,11):
    questao = input(f'Digite a resposta correta da questão {a}: ').strip().upper()
    if a == 1:
        q01 = questao
    elif a ==2:
        q02 = questao
    elif a == 3:
        q03 = questao
    elif a == 4:
        q04 = questao
    elif a == 5:
        q05 = questao
    elif a == 6:
        q06 = questao
    elif a == 7:
        q07 = questao
    elif a == 8:
        q08 = questao
    elif a == 9:
        q09 = questao
    elif a == 10:
        q010 = questao

acertos = 0
cod = 0
alunos_qnt = 1
maior_acerto = 0
menor_acerto = 10
acertos_turma = 0
while True:
    cod = int(input('Informe o seu código de aluno: '))
    for i in range (1,11):
        resposta = input(f'Digite a resposta para a questão {i}: ').upper()

        if i == 1 and resposta == q01 or (i == 2 and resposta == q02) or (i == 3 and resposta == q03) or \
                (i == 4 and resposta == q04) or (i == 5 and resposta == q05) or (i == 6 and resposta == q06) \
                or (i == 7 and resposta == q07) or (i == 8 and resposta == q08) or (i == 9 and resposta == q09)\
                or (i == 10 and resposta == q010):
            acertos += 1
            acertos_turma += 1
    if acertos > maior_acerto:
        maior_acerto = acertos
        aluno_maior = cod
    elif acertos < menor_acerto:
        menor_acerto = acertos
        aluno_menor = cod

    print(acertos)

    aluno = input('Digite SIM, caso outro aluno utilize o sistema:').upper()
    if aluno != 'SIM':
        break
    alunos_qnt += 1
    acertos = 0

print(f'O aluno com a maior acerto foi o {aluno_maior} com : {maior_acerto}'
      f' e o aluno com o menor acerto foi o {aluno_menor} com : {menor_acerto}')
media_notas = (acertos_turma/10)/alunos_qnt
print(f'O total de :{alunos_qnt} Alunos utilizaram o sistema.')
print(f'A Média das Notas da Turma foi de {media_notas:2.f}')
